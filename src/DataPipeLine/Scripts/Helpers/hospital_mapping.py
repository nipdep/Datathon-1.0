import os
import pandas as pd
import json

Directory = 'F:/Deeplearning/Datathon-1.0'
hospital_map = pd.read_csv(Directory+'/data/maps/hospitals.csv',header=None)
#print(hospital_map)

District_hospital_dic = {}
for index in hospital_map.index:
    row = hospital_map.loc[index]
    null_indicator = row.isnull()
    #print(null_indicator)
    hospital_list = []
    for i in range(1,10):
        if(not null_indicator[i]):
            hospital_list.append(row[i])

    District_hospital_dic[row[0]]=hospital_list

print(District_hospital_dic)
try:
    with open(Directory+'/data/maps/hospital_map.json','w') as f:
        json.dump(District_hospital_dic,f)
except:
    print('error')


