
import pandas as pd
import numpy as num
import json
import copy


class Country(dict):
    def __init__(self, name, states_present, stateData, address):
        dict.__init__(self, name=name, states_present=states_present, stateData=stateData, address=address)

def main():
    confirmed_df = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_confirmed_global_cleaned.csv')
    deaths_df = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_deaths_global_cleaned.csv')
    recovered_df = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_recovered_global_cleaned.csv')
    print(confirmed_df)
    print(deaths_df)
    print(recovered_df)
    print (confirmed_df['Country/Region'].size)
    print( type(confirmed_df.columns[5:]))
    # for i in range(662):
    #     print(confirmed_df.columns[5:][i],"---", confirmed_df[confirmed_df.columns[5:][i]][0])

    print(type(confirmed_df['Long'][0]))
    # f=open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/test.json')
    # data=json.load(f)
    # print(data['country'])
    # temp=copy.deepcopy(data['country'][0])
    # for i in range(confirmed_df['Country/Region'].size):
    #     temp['name']=confirmed_df['Country/Region'][i]
    #     # Need to handle this later
    #     temp['states_present']=False
    #     listA=[]
    #     for j in range(1):
    #         stateToAdd= {}
    #         stateToAdd['name']="Not present"
    #         # for k in range()
    #         # stateToAdd['data']=[]




    # with open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/Master.json', 'w',encoding='utf-8') as fp:
    #     json.dump(data, fp,ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
