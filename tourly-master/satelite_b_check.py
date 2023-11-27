import os
from datetime import datetime, timedelta
from urllib.request import urlretrieve


# /home/data/sate/
dir = '/home/data/sate/'
# files = os.listdir(dir)
# print(files)

lstReloadFile = []
swradReloadFile = []

# for file in files:
#     if 'lst' in file:
#         file_size1 = os.path.getsize(dir + file)
#         # print(file_size)
#         if file_size1 < 1000000:
#             file = file.split("_")
#             file = file[5]
#             file = file.split(".")
#             file = file[0]
#             lstReloadFile.append(file)
#     if 'swrad' in file:
#         file_size2 = os.path.getsize(dir + file)
#         if file_size2 < 1000000:
#             file = file.split("_")
#             file = file[5]
#             file = file.split(".")
#             file = file[0]
#             swradReloadFile.append(file)

# print(lstReloadFile)
# print(swradReloadFile)

authKey = 'NMSC9327068932e94c77877854e534d99d14'
for i in lstReloadFile:
    
    url1 = f'http://api.nmsc.kma.go.kr:9080/api/GK2A/LE2/LST/KO/data?date={i}&key={authKey}'
    print(url1)
    print(lstReloadFile)
    exit()
    #/home/data/sate/
    urlretrieve(url1, f'/home/data/sate/gk2a_ami_le2_lst_ko020lc_{i}.nc')
    
for j in swradReloadFile:

    url2 = f'http://api.nmsc.kma.go.kr:9080/api/GK2A/LE2/SWRAD/KO/data?date={j}&key={authKey}'
    # print(url2)

    #/home/data/sate/
    urlretrieve(url2, f'/home/data/sate/gk2a_ami_le2_swrad_ko020lc_{j}.nc')