import requests
import datetime
import mysql.connector

# AWS 744 API 불러오기
authKey = 'SEQk-aWQSbKEJPmlkPmy0w' # auth key
base_url = 'https://apihub.kma.go.kr/api/typ01/url/awsh.php?&help=1&disp=1&stn=744&authKey='

# 현재 시간 구하기
now = datetime.datetime.utcnow()
kstTime = now + datetime.timedelta(hours=9)
updateTime = kstTime - datetime.timedelta(minutes=10)
today = updateTime.strftime("%Y%m%d")
now_Time = updateTime.strftime("%H")

# API url 구성
# url = base_url + authKey + '&tm=' + '202306071600'
url = base_url + authKey + '&tm=' + today + now_Time + '00'
print(url)
exit()

def process_data_and_insert_to_db(url, host, user, password, database, table_name, insert_date):
    try:
        # API 요청
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류 발생 시 예외를 발생시킴

        data = response.text

        # 데이터베이스 연결 설정
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = db.cursor()

        # 데이터를 파싱하고 추출하여 데이터베이스에 저장
        lines = data.split('\n')

        # 필요한 데이터 추출
        base_datetime, id = '', None
        base_date, base_time = '', ''
        TMP, VEC, WSD, RN_DAY, PCP, REH, PA, PS = None, None, None, None, None, None, None, None


        for line in lines:
            if line.startswith("#") :
                continue
            columns = line.split()
            if len(columns) >= 10:
                base_datetime = columns[0]
                base_date = base_datetime[:8]
                base_time = base_datetime[8:]
                id, TMP, VEC, WSD, RN_DAY, PCP, REH, PA, PS = columns[1], float(columns[2]), float(columns[3]), float(columns[4]), \
                                                            float(columns[5]), float(columns[6]), float(columns[7]), \
                                                            float(columns[8]), float(columns[9])
                break


        # DB에 저장
        query = f"INSERT INTO {table_name} (base_datetime, base_date, base_time, id, TMP, VEC, WSD, RN_DAY, PCP, REH, PA, PS, insert_date) " \
                f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (base_datetime, base_date, base_time, id, TMP, VEC, WSD, RN_DAY, PCP, REH, PA, PS, insert_date)
        cursor.execute(query, values)

        # 변경사항 커밋 후 db 닫음
        db.commit()
        cursor.close()
        db.close()

    except requests.exceptions.RequestException as e:
        print("API 요청 오류:", e)
    except mysql.connector.Error as e:
        print("데이터베이스 오류:", e)

def main():
    host = '222.239.231.149'
    user = 'energy'
    password = 'Ctrl-f!1'
    database = 'energy'
    table_name = '744_SITE_1H'

    process_data_and_insert_to_db(url, host, user, password, database, table_name, kstTime)

if __name__ == "__main__":
    main()
