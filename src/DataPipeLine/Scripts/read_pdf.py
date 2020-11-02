import camelot
import pandas as pd
from src.DataPipeLine.Scripts.Clean import *
import os

Directory = 'F:/Deeplearning/Datathon-1.0'


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

            #clean(District_Count_df,Hospital_df,Cumulative_df,1)

            District_Count_df.to_csv(Directory + '/data/District/' + month + '-' + day + 'DC.csv')
            Hospital_df.to_csv(Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv')
            Cumulative_df.to_csv(Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv')

            clean(Directory + '/data/District/' + month + '-' + day + 'DC.csv',
                  Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv',
                  Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv', 1)

            return ({'district_file':Directory + '/data/District/' + month + '-' + day + 'DC.csv',
                  'hospital_file':Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv',
                  'cumulative_file':Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv',
                    'type':1,
                     'success':True})
        else:
            print('different type 1')
            print(dataframe)
            return ({'success': False,
                     'pdf_name':pdf_name,
                     'fail_type':'different type 1'})

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

            #clean(District_Count_df, Hospital_df, Cumulative_df, 3)

            District_Count_df.to_csv(Directory + '/data/District/' + month + '-' + day + 'DC.csv')
            Hospital_df.to_csv(Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv')
            Cumulative_df.to_csv(Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv')

            clean(Directory + '/data/District/' + month + '-' + day + 'DC.csv',
                  Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv',
                  Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv', 3)

            return({'district_file':Directory + '/data/District/' + month + '-' + day + 'DC.csv',
                   'hospital_file':Directory + '/data/Hospital/' + month + '-' + day + 'hos.csv',
                   'cumulative_file':Directory + '/data/Cumulative/' + month + '-' + day + 'cumu.csv',
                    'type':3,
                    'success':True})

        else:
            print('different type 3')
            print(dataframe)
            return({'success':False,
                     'pdf_name':pdf_name,
                     'fail_type':'different type 3'})

    else:
        print('new case')
        return ({'success': False,
                'pdf_name':pdf_name,
                 'fail_type':'new case'})
    # print(district_count_dataframe)

    '''
     try:
        table = camelot.read_pdf(pdf_name)
        print(table.df)
     except:
        print('error')
    '''
