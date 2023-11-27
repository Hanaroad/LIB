# 필요한 모듈 임포트
import pandas as pd
import pymysql
import numpy as np

# pymysql을 통해 데이터베이스에 연결
# conn = pymysql.connect(host='222.239.231.146', user='root', password='A1q2w3e4r!', db='tour')
curs = conn.cursor(pymysql.cursors.DictCursor)

# 로컬 경로에서 엑셀 파일 읽기
file_path = r"C:\Users\admin\Desktop\02. STN_DETAIL_INFO(0905)-순서정렬완료.xlsx"

excel_data = pd.read_excel(file_path)

# NaN 값을 빈 문자열로 대체
excel_data.replace(np.nan, '', inplace=True)

print(excel_data.shape[1])

sql = '''insert into tour.NEW_STN_DETAIL_INFO(stn_no, tel_no, info, theme, h_page, fee, op_time, facility, parking_lot, car, public_transport, hashtag, around_no1, around_no2, around_no3, around_no4)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

for idx in range(len(excel_data)):
    try:
        curs.execute(sql, tuple(excel_data.values[idx]))
    except Exception as ex:
        print(idx, tuple(excel_data.values[idx]))

conn.commit()
conn.close() # 연결 종료
