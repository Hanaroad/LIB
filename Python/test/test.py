import csv
import os
from datetime import datetime, timedelta

# 전남, 충북 위험지수
def get_vilage_index_fcst(stn_code):
    vilage_index_data = []
    vilage_dic_data = {}
    today_data = []
    tomorrow_data = []
    after_tomorrow_data = []
    # 돌풍 위험 지수
    today_gust_idx = []
    tomorrow_gust_idx = []
    after_tomorrow_gust_idx = []
    # 서리 위험 지수
    today_frost_idx = []
    tomorrow_frost_idx = []
    after_tomorrow_frost_idx = []
    #  가뭄 위험 지수
    today_dry_idx = []
    tomorrow_dry_idx = []
    after_tomorrow_dry_idx = []

    file_path = os.path.join(os.path.dirname(__file__), 'vilageFcst.csv')

    with open(file_path, encoding='utf-8') as file:
        reader = csv.reader(file)

        header = next(reader)

        now = datetime.now()
        today = now.strftime('%Y%m%d')


        first_row = next(reader)
        
        today_date = datetime.strptime(first_row[3], '%Y%m%d')
        next1_date = today_date + timedelta(days=1)
        next2_date = today_date + timedelta(days=2)

        today_str = datetime.strftime(today_date, '%Y%m%d')
        next1_str = datetime.strftime(next1_date, '%Y%m%d')
        next2_str = datetime.strftime(next2_date, '%Y%m%d')

        print(today_str, next1_str, next2_str)
        exit()


        for line in reader:
            if line[0] == stn_code and line[19] == 'Y' and line[3] == today_str :
                gust = int(line[22])
                frost = int(line[23])
                dry = int(line[24])
                today_gust_idx.append(gust)
                today_frost_idx.append(frost)
                today_dry_idx.append(dry)
            if line[0] == stn_code and line[19] == 'Y' and line[3] == next1_str :
                gust = int(line[22])
                frost = int(line[23])
                dry = int(line[24])
                tomorrow_gust_idx.append(gust)
                tomorrow_frost_idx.append(frost)
                tomorrow_dry_idx.append(dry)
            if line[0] == stn_code and line[19] == 'Y' and line[3] == next2_str :
                gust = int(line[22])
                frost = int(line[23])
                dry = int(line[24])
                after_tomorrow_gust_idx.append(gust)
                after_tomorrow_frost_idx.append(frost)
                after_tomorrow_dry_idx.append(dry)
        # 돌풍 최대치
        try:
            vilage_dic_data['today_gust'] = max(today_gust_idx)
            vilage_dic_data['tomorrow_gust'] = max(tomorrow_gust_idx)
            vilage_dic_data['after_tomorrow_gust'] = max(after_tomorrow_gust_idx)
        except:
            vilage_dic_data['today_gust'] = 0
            vilage_dic_data['tomorrow_gust'] = 0
            vilage_dic_data['after_tomorrow_gust'] = 0

        # 서리 최대치
        try:
            vilage_dic_data['today_frost'] = max(today_frost_idx)
            vilage_dic_data['tomorrow_frost'] = max(tomorrow_frost_idx)
            vilage_dic_data['after_tomorrow_frost'] = max(after_tomorrow_frost_idx)
        except:
            vilage_dic_data['today_frost'] = 0
            vilage_dic_data['tomorrow_frost'] = 0
            vilage_dic_data['after_tomorrow_frost'] = 0

        # 가뭄 최대치
        try:
            vilage_dic_data['today_dry'] = max(today_dry_idx)
            vilage_dic_data['tomorrow_dry'] = max(tomorrow_dry_idx)
            vilage_dic_data['after_tomorrow_dry'] = max(after_tomorrow_dry_idx)
        except:
            vilage_dic_data['today_dry'] = 0
            vilage_dic_data['tomorrow_dry'] = 0
            vilage_dic_data['after_tomorrow_dry'] = 0

        vilage_index_data.append(vilage_dic_data)
    return vilage_index_data




get_vilage_index_fcst('4300000000')