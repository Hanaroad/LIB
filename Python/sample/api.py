#!/root/.pyenv/versions/3.6.4/bin/python
#-*- encoding:utf8 -*-#
# import common
import requests
import json
from datetime import timedelta, datetime
import os
from ast import literal_eval
import math
# import wget


log_date = datetime.now().strftime('%Y%m%d %H:%M:%S')
#시작일
date_s = '20200101'
#종료일
date_e = '20200101'

#수집시간 설정
#hr_list = ['00', '03', '06', '09', '12', '15', '18', '21']
hr_list = ['00']

def start() : 
	servicekey = "b33b6583c8219d51576fbb9c3378ef50bbfc51a8da9340515ab23d53650d93985244d7c9863537aaf1ccf6fb6021ac86a636ba264ac0ba023cc8af5c2d284383"
	url_ori = "http://203.247.66.28/url"
	sub_url ="/nwp_file_down.php"
	new = "?nwp=l015"
	sub = "&sub=unis"
	tmfc = "&tmfc="
	hh_ef = "&hh_ef="
	authKey = "&authKey="+servicekey
	

	date_object = datetime.strptime(date_s, '%Y%m%d')
	sum_1_day = timedelta(days=(+1))

	while int((date_object).strftime('%Y%m%d')) <=int(date_e) : 
		
		for idx, row in enumerate(hr_list):
			set_date = str(date_object.strftime('%Y%m%d'))+hr_list[idx] 
			for i in range(0, 49) : 
				#i는 0~48까지 hr 
				#option = " -O ./l015_unis_h"+set_h(i)+"_"+str(set_date)+".gb2"
				url = url_ori
				url += sub_url
				url += new
				url += sub
				url += tmfc + set_date
				url += hh_ef + set_h(i)
				url += authKey
				#url += option

				print(url)
				exit()

				copy_name = "l015_unis_h"+set_h(i)+"_"+str(set_date)+".gb2"
				#requests.get(url)
				wget.download(url, copy_name)

				url =""
			#set_date = (date_object).strftime('%Y%m%d')+hr_list[idx]
			#print(str(date_object.strftime('%Y%m%d'))+hr_list[idx])

		date_object = (date_object+sum_1_day)

def set_h(val):

	rtn = ''
	if(val<10)	:
		rtn = '0'+str(val)
	else :
		rtn = str(val)
	#print(rtn)
	return rtn


if __name__ == '__main__':
	
	start()