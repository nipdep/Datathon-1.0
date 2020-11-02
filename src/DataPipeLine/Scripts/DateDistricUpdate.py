import pandas as pd
import os
import json
from src.DataPipeLine.Scripts.Helpers.dateformat import *

Directory = 'F:/Deeplearning/Datathon-1.0'
def split(word):
    return [char for char in word]

def DateDistricUpdate(date = dateformat()):
    log = {}
    if (not os.path.exists(Directory + '/data/main_data/DateDistric.csv')):
        # date_distric_df = pd.DataFrame(columns=['ID','Date','District','Suspected_Local','Suspected_Foreign','Suspected_Total','Temperature','Immobility']).to_csv(Directory+'/data/DateDistric.csv')
        date_distric_df = pd.DataFrame(
            columns=['ID', 'Date', 'District', 'Suspected_Local', 'Suspected_Foreign', 'Suspected_Total'])
        #date_distric_df.to_csv(Directory + '/data/DateDistric.csv')
    else:
        date_distric_df = pd.read_csv(Directory + '/data/main_data/DateDistric.csv')

    try:
        with open(Directory + '/data/maps/hospital_map.json', 'r') as f:
            hospital_map = json.load(f)
    except:
        print('Error')

    print(hospital_map)
    filename = Directory + '/data/Hospital/'+ date[0]+'-'+date[1]+'hos.csv'
    print(filename)
    [month, day] =date
    print(date)
    print(' ')
    log['filename'] = filename

    if(not os.path.exists(filename)):
        log['success'] = False
        log['Failure_reason'] = 'file not exist yet'
        return log

    df = pd.read_csv(filename)
    # count = 0
    district_df = pd.DataFrame(
        columns=['ID', 'Date', 'District', 'Suspected_Local', 'Suspected_Foreign', 'Suspected_Total'])
    for district in hospital_map.keys():
        # print(district)
        list_hospitals = hospital_map[district]
        sl_today = 0
        for_today = 0
        total_today = 0

        for hospital in list_hospitals:
            row = df.loc[df.Hospital == hospital]
            # print(hospital)
            if (row.empty):
                print(hospital)
                continue
            # print('row :- ',row)
            # print('value - ',row.at[row.index[0],'SL_Today'])
            sl_today += int(row.at[row.index[0], 'SL_Today'])
            for_today += int(row.at[row.index[0], 'Foreign_Today'])
            total_today += int(row.at[row.index[0], 'Total_Today'])

        district_df = district_df.append({'ID': month + day + '_' + district,
                                          'Date': month + '-' + day,
                                          'District': district,
                                          'Suspected_Local': sl_today,
                                          'Suspected_Foreign': for_today,
                                          'Suspected_Total': total_today}, ignore_index=True)


        # count += 1
        # print('array data',[month+day+'_'+district,
        #                    month+'-'+day,
        #                    district,
        #                    sl_today,
        #                    for_today,
        #                    total_today
        #                    ])
    # print(district_df)
    log['update_size']=len(district_df)
    date_distric_df = date_distric_df.append(district_df)

    log['Total_size'] = len(date_distric_df)
    print(date_distric_df)

    date_distric_df.to_csv(Directory + '/data/main_data/DateDistric.csv')
    log['success'] = True
    return(log)
