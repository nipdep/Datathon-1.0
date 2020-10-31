import pandas as pd
import os
import json

Directory = 'F:/Deeplearning/Datathon-1.0'
def split(word):
    return [char for char in word]

def DateDistric():
    if (not os.path.exists(Directory + '/data/DateDistric.csv')):
        # date_distric_df = pd.DataFrame(columns=['ID','Date','District','Suspected_Local','Suspected_Foreign','Suspected_Total','Temperature','Immobility']).to_csv(Directory+'/data/DateDistric.csv')
        date_distric_df = pd.DataFrame(
            columns=['ID', 'Date', 'District', 'Suspected_Local', 'Suspected_Foreign', 'Suspected_Total'])
        #date_distric_df.to_csv(Directory + '/data/DateDistric.csv')
    else:
        date_distric_df = pd.read_csv(Directory + '/data/DateDistric.csv')

    try:
        with open(Directory + '/data/maps/hospital_map.json', 'r') as f:
            hospital_map = json.load(f)
    except:
        print('Error')

    print(hospital_map)
    list_hospital_files = os.listdir(Directory + '/data/Hospital')
    if ('.ipynb_checkpoints' in list_hospital_files):
        list_hospital_files.remove('.ipynb_checkpoints')

    print(list_hospital_files)
    for filename in list_hospital_files:
        [month, day] = filename[:5].split('-')
        print(filename[:5].split('-'))
        print(' ')

        df = pd.read_csv(Directory + '/data/Hospital/' + filename)
        #count = 0
        district_df = pd.DataFrame(
            columns=['ID', 'Date', 'District', 'Suspected_Local', 'Suspected_Foreign', 'Suspected_Total'])
        for district in hospital_map.keys():
            #print(district)
            list_hospitals = hospital_map[district]
            sl_today = 0
            for_today = 0
            total_today = 0


            for hospital in list_hospitals:
                row = df.loc[df.Hospital == hospital]
                #print(hospital)
                if(row.empty):
                    print(hospital)
                    continue
                #print('row :- ',row)
                #print('value - ',row.at[row.index[0],'SL_Today'])
                sl_today += int(row.at[row.index[0],'SL_Today'])
                for_today += int(row.at[row.index[0],'Foreign_Today'])
                total_today += int(row.at[row.index[0],'Total_Today'])

            district_df=district_df.append({'ID':month+day+'_'+district,
                                'Date':month+'-'+day,
                                'District':district,
                                'Suspected_Local':sl_today,
                                'Suspected_Foreign':for_today,
                                'Suspected_Total':total_today},ignore_index=True)

            #count += 1
            #print('array data',[month+day+'_'+district,
            #                    month+'-'+day,
            #                    district,
            #                    sl_today,
            #                    for_today,
            #                    total_today
            #                    ])
        #print(district_df)
        date_distric_df=date_distric_df.append(district_df)
        #print(date_distric_df)
        print('*** \n \n')
    print(date_distric_df)
    date_distric_df.to_csv(Directory + '/data/DateDistric.csv')

DateDistric()
