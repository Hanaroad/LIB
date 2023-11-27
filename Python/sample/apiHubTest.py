import datetime
import requests

# 년월일시(오늘, 내일, 모레)
now = datetime.datetime.utcnow()
kstTime = now + datetime.timedelta(hours=9)
today = kstTime.strftime("%Y%m%d")
year = int(kstTime.strftime("%Y"))
month = int(kstTime.strftime("%m"))
day = int(kstTime.strftime("%d"))
tomorrow_day = kstTime + datetime.timedelta(days=1) # 내일
after_tomorrow_day = kstTime + datetime.timedelta(days=2) # 모레
tomorrow = int(tomorrow_day.strftime("%Y%m%d"))
after_tomorrow = int(after_tomorrow_day.strftime("%Y%m%d"))
tomorrow_str = (tomorrow_day.strftime("%Y%m%d"))
after_tomorrow_str = (after_tomorrow_day.strftime("%Y%m%d"))
time = int(kstTime.strftime("%H"))

auth_key = "b33b6583c8219d51576fbb9c3378ef50bbfc51a8da9340515ab23d53650d93985244d7c9863537aaf1ccf6fb6021ac86a636ba264ac0ba023cc8af5c2d284383"

# 기존 url
기존 = 'http://203.247.66.28/url/sfc_aws_day.php?obs=rn_day&disp=0&help=0&tm1=20230418&stn=710&authKey=b33b6583c8219d51576fbb9c3378ef50bbfc51a8da9340515ab23d53650d93985244d7c9863537aaf1ccf6fb6021ac86a636ba264ac0ba023cc8af5c2d284383'
# 바뀐 url
url2 = 'https://apihub-pub.kma.go.kr/api/typ01/cgi-bin/aws/nph-aws_min_obj?obs=rn_day&tm=201709181230&obj=mq&map=D3&grid=1&stn=710&gov=&authKey=b33b6583c8219d51576fbb9c3378ef50bbfc51a8da9340515ab23d53650d93985244d7c9863537aaf1ccf6fb6021ac86a636ba264ac0ba023cc8af5c2d284383'
# 바뀐 url로 수정
url1 = 'https://apihub-pub.kma.go.kr/api/typ01/cgi-bin/aws/nph-aws_min_obj?obs=rn_day&disp=0&help=0&tm1=20230418&stn=710&authKey=b33b6583c8219d51576fbb9c3378ef50bbfc51a8da9340515ab23d53650d93985244d7c9863537aaf1ccf6fb6021ac86a636ba264ac0ba023cc8af5c2d284383'


https://apihub.kma.go.kr/api/typ01/url/sfc_aws_day.php?tm2=20230418&obs=rn_day&stn=710&disp=0&help=0&authKey=MIgxK1f5QjaIMStX-dI2PQ
https://apihub.kma.go.kr/api/typ01/url/sfc_aws_day.php?obs=rn_day&disp=0&help=0&tm2=20230418&stn=710&authKey=MIgxK1f5QjaIMStX-dI2PQ

# 60일치 강수량 API
def get_data(stn):
   try:
      
      now = datetime.datetime.now()
      tm1 = ( now - datetime.timedelta(days=65) ).strftime("%Y%m%d")
      
      url = "http://203.247.66.28/url/sfc_aws_day.php?obs=rn_day&disp=0&help=0"
      # url = "https://apihub.kma.go.kr/api/typ01/sfc_aws_day.php?obs=rn_day&disp=0&help=0"
      url += "&tm1=" +  tm1
      url += "&stn=" +  stn
      url += "&authKey=" + auth_key

      response = requests.get(url)
      result_code = response.status_code
      result_test = response.text
      value_list = []
      print(result_code)
      print(url)
      exit()

      if (result_code == 200):

         rtn_val = result_test.split("\n")

         for idx in range(len(rtn_val)):

            if idx > 2 and idx < len(rtn_val) -2:

               temp_list = rtn_val[idx].split(" ")
               temp_list = ' '.join(temp_list).split()
               value_list.append(float(temp_list[-2]))
      return value_list
   
   except Exception as e:
      print(stn + e)

get_data("710")