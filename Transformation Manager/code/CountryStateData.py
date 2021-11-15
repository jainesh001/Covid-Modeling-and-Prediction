import pandas as pd
import numpy as num
import json





def main():
    confirmed_df = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_confirmed_global_cleaned.csv')
    deaths_df = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_deaths_global_cleaned.csv')
    recovered_df = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_recovered_global_cleaned.csv')
    print(confirmed_df)
    print(deaths_df)
    print(recovered_df)

    print(confirmed_df['Province/State'].size)

    listOfCountries = []
    listOfState = []
    temp = {}
    current_state=""
    arrangeInTwoListStateAndCountry(confirmed_df,listOfCountries,listOfState)
    deriveCountryStateListDictonary(listOfCountries,listOfState,temp)
    print(listOfCountries)
    print(listOfState)
    print(temp)
    with open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/stateCountryDataForConfirmed.json','w', encoding='utf-8') as f:
        json.dump(temp, f, ensure_ascii=False, indent=4)

    listOfCountries = []
    listOfState = []
    temp = {}
    arrangeInTwoListStateAndCountry(deaths_df, listOfCountries, listOfState)
    deriveCountryStateListDictonary(listOfCountries, listOfState,temp)
    print(listOfCountries)
    print(listOfState)
    print(temp)
    with open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/stateCountryDataForDeath.json','w', encoding='utf-8') as f:
        json.dump(temp, f, ensure_ascii=False, indent=4)

    listOfCountries = []
    listOfState = []
    temp = {}
    arrangeInTwoListStateAndCountry(recovered_df, listOfCountries, listOfState)
    deriveCountryStateListDictonary( listOfCountries, listOfState,temp)
    print(listOfCountries)
    print(listOfState)
    print(temp)

    print(json.dumps(temp))
    with open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/stateCountryDataForRecovered.json', 'w', encoding='utf-8') as f:
        json.dump(temp, f, ensure_ascii=False, indent=4)




def deriveCountryStateListDictonary(listOfCountries,listOfState,temp):
    tempList = []
    for i in range(len(listOfState)):
        if i == 0:
            tempList.append(listOfState[i])
        if i >= 1:
            if listOfCountries[i] == listOfCountries[i - 1]:
                tempList.append(listOfState[i])
                if i == len(listOfState) - 1:
                    temp[listOfCountries[i]] = tempList
            elif i >= 1:
                temp[listOfCountries[i - 1]] = tempList
                tempList = []
                tempList.append(listOfState[i])



def arrangeInTwoListStateAndCountry(csvFile,listOfCountries,listOfState):
    for i in range(csvFile['Province/State'].size):
        if not pd.isna(csvFile['Province/State'][i]):
            listOfCountries.append(csvFile['Country/Region'][i])
            listOfState.append(csvFile['Province/State'][i])

if __name__ == "__main__":
    main()
