import os
import json
import datetime
import luigi
import camelot
import pandas as pd
from luigi.contrib import mysqldb
from luigi.util import requires, inherits, common_params

Directory = 'F:/Deeplearning/Datathon-1.0'
pdf_dir = Directory + '/data/daily_pdf'
log_dir = Directory + '/src/DataPipeLine/Flow/logs'


def split(word):
    return [char for char in word]


def removeWhiteCharacters(string):
    # print(string)
    string = string.strip()
    word = split(string)
    if ('\n' in word):
        print(string)
        word.remove('\n')
        word = ''.join(word)
        print(word)
        return (word)

    if ("'" in word):
        print(string)
        word.remove("'")
        word = ''.join(word)
        print(word)
        return (word)

    if ("’" in word):
        print(string)
        word.remove("’")
        word = ''.join(word)
        print(word)
        return (word)

    return (string)


def clean(dis, hos, cumu, type):
    dis_df = pd.read_csv(dis)
    hos_df = pd.read_csv(hos)
    cumu_df = pd.read_csv(cumu)

    # dis_df = dis_df.dropna(how='any', axis=0, inplace=True)
    # hos_df = hos_df.dropna(how='any', axis=0, inplace=True)
    # cumu_df = cumu_df.dropna(how='any', axis=0, inplace=True)

    dis_df = dis_df.dropna(how='any', axis=0)[['District', 'Count']]
    dis_df = dis_df.loc[:, ~dis_df.columns.str.contains('^Unnamed')]
    dis_df = dis_df.applymap(removeWhiteCharacters)

    hos_df = hos_df.dropna(how='any', axis=0)[['Hospital', 'SL_Today', 'Foreign_Today', 'Total_Today']].copy()
    hos_df = hos_df.loc[:, ~hos_df.columns.str.contains('^Unnamed')]
    hos_df = hos_df.applymap(removeWhiteCharacters)

    cumu_df = cumu_df.dropna(how='any', axis=0)[['Hospital', 'SL_Total', 'Foreign_Total', 'Total']].copy()
    cumu_df = cumu_df.loc[:, ~cumu_df.columns.str.contains('^Unnamed')]
    cumu_df = cumu_df.applymap(removeWhiteCharacters)

    dis_df.to_csv(dis)
    hos_df.to_csv(hos)
    cumu_df.to_csv(cumu)

    # return [dis_df,hos_df,cumu_df]


def getPDF(pdf_name):
    [month, day] = pdf_name[-9:-4].split('-')
    print(pdf_name[-9:-4].split('-'))
    '''
    if(not os.path.exists(Directory+'/data/District_Count.csv')):
        pd.DataFrame(data=None,columns=['District','Count']).to_csv(Directory+'/data/District_Count.csv')

    if (not os.path.exists(Directory + '/data/Hospital.csv')):
        pd.DataFrame(data=None, columns=['Hospital','SL_Today','Foreign_Today','Total_Today']).to_csv(Directory + '/data/Hospital.csv')

    if (not os.path.exists(Directory + '/data/Cumulative.csv')):
        pd.DataFrame(data=None, columns=['Hospital','SL_Total','Foreign_Total','Total']).to_csv(Directory + '/data/Hospital.csv')

    District_Count_df = pd.read_csv(Directory+'/data/District_Count.csv')
    Hospital_df = pd.read_csv(Directory + '/data/Hospital.csv')
    Cumulative_df = pd.read_csv(Directory + '/data/Cumulative.csv')
    '''
    District_Count_df = pd.DataFrame(columns=['District', 'Count'])
    Hospital_df = pd.DataFrame(columns=['Hospital', 'SL_Today', 'Foreign_Today', 'Total_Today'])
    Cumulative_df = pd.DataFrame(columns=['Hospital', 'SL_Total', 'Foreign_Total', 'Total'])

    table = camelot.read_pdf(pdf_name, pages='2')
    if (len(table) == 1):
        dataframe = table[0].df
        if (len(dataframe.columns) >= 13):
            District_Count_df.District = dataframe.loc[:, 11]
            District_Count_df.Count = dataframe.loc[:, 12]
            Hospital_df.Hospital = dataframe.loc[:, 1]
            Hospital_df.SL_Today = dataframe.loc[:, 5]
            Hospital_df.Foreign_Today = dataframe.loc[:, 6]
            Hospital_df.Total_Today = dataframe.loc[:, 7]
            Cumulative_df.Hospital = dataframe.loc[:, 1]
            Cumulative_df.SL_Total = dataframe.loc[:, 2]
            Cumulative_df.Foreign_Total = dataframe.loc[:, 3]
            Cumulative_df.Total = dataframe.loc[:, 4]
            # print(District_Count_df)
            '''
            for index in dataframe.index:
                row = dataframe.loc[index]

                print(row)
                District_Count_df.append({'District': row[11], 'Count': row[12]})
                Hospital_df.append({'Hospital':row[1], 'SL_Today':row[5], 'Foreign_Today':row[6], 'Total_Today':row[7]})
                Cumulative_df.append({'Hospital':row[1], 'SL_Total':row[2], 'Foreign_Total':row[3], 'Total':row[4]})
                # print(type(row[11]))
                # print(row[12])
                # print(type(row[12]))
                # if(type(row[11]) == str and type(row[12]) == str):
                # print(row)
                # print (row)
                # if(row[1])
            '''

            # clean(District_Count_df,Hospital_df,Cumulative_df,1)

            District_Count_df.to_csv(Directory + '/data/District/' + month + '-' + day + 'DC.csv')
            Hospital_df.to_csv(Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv')
            Cumulative_df.to_csv(Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv')

            clean(Directory + '/data/District/' + month + '-' + day + 'DC.csv',
                  Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv',
                  Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv', 1)

            return ({'district_file': Directory + '/data/District/' + month + '-' + day + 'DC.csv',
                     'hospital_file': Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv',
                     'cumulative_file': Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv',
                     'type': 1,
                     'success': True})
        else:
            print('different type 1')
            print(dataframe)
            return ({'success': False,
                     'pdf_name': pdf_name,
                     'fail_type': 'different type 1'})

    elif (len(table) == 3):

        dataframe = table[0].df
        District_Count_df = pd.DataFrame(columns=['District', 'Count'])
        District_Count_df.District = dataframe.loc[:, 0]
        District_Count_df.Count = dataframe.loc[:, 1]

        dataframe = table[1].df
        if (len(dataframe.columns) >= 8):
            Hospital_df = pd.DataFrame(columns=['Hospital', 'SL_Today', 'Foreign_Today', 'Total_Today'])
            Cumulative_df = pd.DataFrame(columns=['Hospital', 'SL_Total', 'Foreign_Total', 'Total'])

            Hospital_df.Hospital = dataframe.loc[:, 1]
            Hospital_df.SL_Today = dataframe.loc[:, 5]
            Hospital_df.Foreign_Today = dataframe.loc[:, 6]
            Hospital_df.Total_Today = dataframe.loc[:, 7]
            Cumulative_df.Hospital = dataframe.loc[:, 1]
            Cumulative_df.SL_Total = dataframe.loc[:, 2]
            Cumulative_df.Foreign_Total = dataframe.loc[:, 3]
            Cumulative_df.Total = dataframe.loc[:, 4]

            # clean(District_Count_df, Hospital_df, Cumulative_df, 3)

            District_Count_df.to_csv(Directory + '/data/District/' + month + '-' + day + 'DC.csv')
            Hospital_df.to_csv(Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv')
            Cumulative_df.to_csv(Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv')

            clean(Directory + '/data/District/' + month + '-' + day + 'DC.csv',
                  Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv',
                  Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv', 3)

            return ({'district_file': Directory + '/data/District/' + month + '-' + day + 'DC.csv',
                     'hospital_file': Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv',
                     'cumulative_file': Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv',
                     'type': 3,
                     'success': True})

        else:
            print('different type 3')
            print(dataframe)
            return ({'success': False,
                     'pdf_name': pdf_name,
                     'fail_type': 'different type 3'})

    else:
        print('new case')
        return ({'success': False,
                 'pdf_name': pdf_name,
                 'fail_type': 'new case'})
    # print(district_count_dataframe)

    '''
     try:
        table = camelot.read_pdf(pdf_name)
        print(table.df)
     except:
        print('error')
    '''


def dateformat():
    today = datetime.datetime.now()
    month = today.month
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    day = today.day
    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)

    return ([month, day])


class WebScrapingExtract(luigi.Task):

    def __init__(self, *args, **kwargs):
        """ something if needed"""
        super().__init__(*args, **kwargs)
        self.current_date = dateformat()
        self.log_file = log_dir + '/' + self.current_date[0] + '-' + self.current_date[1] + 'extract.json'

    def requires(self):
        """ Since First Layer not required by anything """

    def output(self):
        """ Output a data but saving file recommended  """
        return luigi.LocalTarget(self.log_file)

    def run(self):
        """ Nipun's web scraping code """
        print(os.path.exists(pdf_dir + '/' + self.current_date[0] + '-' + self.current_date[1] + '.pdf'))
        if (os.path.exists(pdf_dir + '/' + self.current_date[0] + '-' + self.current_date[1] + '.pdf')):
            details = getPDF(pdf_dir + '/' + self.current_date[0] + '-' + self.current_date[1] + '.pdf')
        else:
            print('pdf not exist yet')
            print('pdf path checked :- ', pdf_dir + '/' + self.current_date[0] + '-' + self.current_date[1] + '.pdf')
            details = {'success': False,
                        'status': 'pdf not exist yet',
                       'path_detail': pdf_dir + '/' + self.current_date[0] + '-' + self.current_date[1] + '.pdf'}
        # process

        if(details['success']):
            try:
                with self.output().open(mode='w') as f:
                    json.dump(details, f)
            except:
                print('error')











class WebScrapingTransform(luigi.Task):
    def __init__(self, *args, **kwargs):
        """ something if needed"""
        super().__init__(*args, **kwargs)
        self.current_date = dateformat()
        self.log_file = log_dir + '/' + self.current_date[0] + '-' + self.current_date[1] + 'transform.json'

    def requires(self):
        """ Since First Layer not required by anything """
        return WebScrapingExtract()

    def output(self):
        """ Output a Json file most probably """
        return luigi.LocalTarget(self.log_file)

    def run(self):
        """ required transforms """

        """ APPLY TRANSFORM IF ANY """
        details = {'success': True,'status': 'no transforms yet'}

        if (details['success']):
            try:
                with self.output().open(mode='w') as f:
                    json.dump(details, f)
            except:
                print('error')






def split(word):
    return [char for char in word]

def DateDistricUpdate(date = dateformat()):
    log = {}
    if (not os.path.exists(Directory + '/data/DateDistric.csv')):
        # date_distric_df = pd.DataFrame(columns=['ID','Date','District','Suspected_Local','Suspected_Foreign','Suspected_Total','Temperature','Immobility']).to_csv(Directory+'/data/DateDistric.csv')
        date_distric_df = pd.DataFrame(
            columns=['ID', 'Date', 'District', 'Suspected_Local', 'Suspected_Foreign', 'Suspected_Total','TotalInfected'])
        #date_distric_df.to_csv(Directory + '/data/DateDistric.csv')
    else:
        date_distric_df = pd.read_csv(Directory + '/data/DateDistric.csv')

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

    print(not os.path.exists(filename))
    if(not os.path.exists(filename)):
        log['success'] = False
        log['Failure_reason'] = 'file not exist yet'
        return log

    df = pd.read_csv(filename)
    print(filename[:-7] + 'DC.csv')
    infected_filename = filename[-12:-7] + 'DC.csv'
    infected_df = pd.read_csv(Directory+'/data/District/'+infected_filename)
    # count = 0
    #print(infected_df)
    district_df = pd.DataFrame(
        columns=['ID', 'Date', 'District', 'Suspected_Local', 'Suspected_Foreign', 'Suspected_Total','TotalInfected'])
    for district in hospital_map.keys():
        #print(district)
        dis_row = infected_df.loc[infected_df.District == district.upper()]
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
                                          'Suspected_Total': total_today,
                                            'TotalInfected': int(dis_row.at[dis_row.index[0], 'Count'])}, ignore_index=True)


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

    date_distric_df.to_csv(Directory + '/data/DateDistric.csv')
    log['success'] = True
    return(log)






class WebScrapingLoad(luigi.Task):
    def __init__(self, *args, **kwargs):
        """ something if needed"""
        super().__init__(*args, **kwargs)
        self.current_date = dateformat()
        self.log_file = log_dir + '/' + self.current_date[0] + '-' + self.current_date[1] + 'load.json'

    def requires(self):
        """ Since First Layer not required by anything """
        return WebScrapingTransform()

    def output(self):
        """ Output a Json file most probably """
        return luigi.LocalTarget(self.log_file)

    def run(self):
        print('hello')
        details = DateDistricUpdate()

        if (details['success']):
            try:
                with self.output().open(mode='w') as f:
                    json.dump(details, f)
            except:
                print('error')


if __name__ == '__main__':
    luigi.run()
