import pandas as pd
import os

Directory = 'F:/Deeplearning/Datathon-1.0'

def split(word):
    return [char for char in word]

def removeWhiteCharacters(string):
    #print(string)
    string = string.strip()
    word = split(string)
    if ('\n' in word):
        print(string)
        word.remove('\n')
        word = ''.join(word)
        print(word)
        return(word)

    if ("'" in word):
        print(string)
        word.remove("'")
        word = ''.join(word)
        print(word)
        return(word)

    if ("’" in word):
        print(string)
        word.remove("’")
        word = ''.join(word)
        print(word)
        return(word)

    return(string)

def clean(dis,hos,cumu,type):
    dis_df = pd.read_csv(dis)
    hos_df = pd.read_csv(hos)
    cumu_df = pd.read_csv(cumu)

    #dis_df = dis_df.dropna(how='any', axis=0, inplace=True)
    #hos_df = hos_df.dropna(how='any', axis=0, inplace=True)
    #cumu_df = cumu_df.dropna(how='any', axis=0, inplace=True)

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

    #return [dis_df,hos_df,cumu_df]

