from datetime import datetime, timedelta
from urllib.request import urlretrieve


#################################################################
#UTC 시간 o
dt_utc = str(datetime.utcnow().replace(microsecond=0))
# print(f"UTC 기준 시간 : {dt_utc}")
# utcPrev1H = str(dt_utc - timedelta(hours=1))
# print(f"UTC 기준 1시간 전 : {utcPrev1H}")

str_utc = dt_utc.split(' ')

date1 = str_utc[0].split("-")
date2 = str_utc[1].split(":")
utc_now_date = date1[0] + date1[1] + date1[2] + date2[0] + '00'
print(utc_now_date)
exit()
# print(utc_now_date)


# S4. 천리안위성2A호 인공지능(AI) 기반 일사량
# url : http://203.247.66.28/url/sat_file_down2.php?lvl=l2&dat=ai-dsr&are=ko&tm=202107100700&typ=bin&authKey=b33b6583c8219d51576fbb9c3378ef50bbfc51a8da9340515ab23d53650d93985244d7c9863537aaf1ccf6fb6021ac86a636ba264ac0ba023cc8af5c2d284383
# 파일명 : gk2a_ami_le2_ai-dsr_ko020lc_202206080800.nc

########################################################
#만약에 데이터가 생성되지 않은 경우 해당 변수를 체크!
YYYY = '2022'
MM = '06'
DD = '19'
HH = '10'
#utc_now_date = YYYY + MM + DD + HH + '00'
########################################################

# 타입 : bin, img
type = 'bin'
# 확장자 : nc, png
extend = 'nc'

authKey = 'b33b6583c8219d51576fbb9c3378ef50bbfc51a8da9340515ab23d53650d93985244d7c9863537aaf1ccf6fb6021ac86a636ba264ac0ba023cc8af5c2d284383'
url = f'http://203.247.66.28/url/sat_file_down2.php?lvl=l2&dat=ai-dsr&are=ko&tm={utc_now_date}&typ={type}&authKey={authKey}'
#print(url)

#/home/data/sate/
urlretrieve(url, f'/home/data/sate/gk2a_ami_le2_ai-dsr_ko020lc_{utc_now_date}.nc')