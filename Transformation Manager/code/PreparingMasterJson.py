import pandas as pd
import numpy as num
import json
import copy


class Country(dict):
    def __init__(self, name, states_present, stateData, address):
        dict.__init__(self, name=name, states_present=states_present, stateData=stateData, address=address)


def main():
    confirmed_df = pd.read_csv(
        'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_confirmed_global_cleaned.csv')
    deaths_df = pd.read_csv(
        'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_deaths_global_cleaned.csv')
    recovered_df = pd.read_csv(
        'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_recovered_global_cleaned.csv')

    # Load sample json for schema
    f = open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/test.json')
    # Load the json with load method into data
    data = json.load(f)

    # Temporary variable to handle recovered cases as there is no recovered cases after 8/4/2021
    u = -1
    # Temporary flag to notify when to load 'u'
    flag = True
    for i in range(confirmed_df['Country/Region'].size):
        if flag:
            u = u + 1
        # Making a deep copy of the first sample schema from the data(structure)
        temp = copy.deepcopy(data['country'][0])
        #Load the variable from csv to json e
        temp['name'] = confirmed_df['Country/Region'][i]
        temp['Lat'] = float(confirmed_df['Lat'][i])
        temp['Long'] = float(confirmed_df['Long'][i])
        # Need to handle this later
        temp['states_present'] = False
        listA = []
        # Iterate and set the Date-confimedcases-deaths-recovered
        for j in range(1):
            stateToAdd = {}
            stateToAdd['name'] = "Not present"
            dateData = []
            for k in range(int(confirmed_df.columns[5:].size)):
                dateDict = {}
                dateDict['Date'] = confirmed_df.columns[5:][k]
                dateDict['confirmed'] = int(confirmed_df[confirmed_df.columns[5:][k]][i])
                dateDict['deaths'] = int(deaths_df[deaths_df.columns[5:][k]][i])
                #Modification to handle recovered cases as there is no state for canada available
                if str(confirmed_df['Country/Region'][i]) != str(recovered_df['Country/Region'][u]):
                    dateDict['recovered'] = 0
                    print(confirmed_df['Country/Region'][i], "--->", recovered_df['Country/Region'][u])
                    flag = False
                # if both the country/state matches then load the recovered cases
                else:
                    if u < recovered_df['Country/Region'].size:
                        dateDict['recovered'] = int(recovered_df[recovered_df.columns[5:][k]][u])
                        flag = True
                dateData.append(dateDict)

            stateToAdd['data'] = dateData
            listA.append(stateToAdd)

        temp['stateData'] = listA
        data['country'].append(temp)

    # To remove the sample schema stucture from the file
    data['country'].pop(0)
    # Saving data into the file
    with open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/Master.json', 'w',
              encoding='utf-8') as fp:
        json.dump(data, fp)


if __name__ == "__main__":
    main()
