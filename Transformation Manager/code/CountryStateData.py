import pandas as pd
import numpy as num
import json


# Primary purpose is to figure out what states are available for what country
def main():
    confirmed_df = pd.read_csv(
        'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_confirmed_global_cleaned.csv')
    deaths_df = pd.read_csv(
        'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_deaths_global_cleaned.csv')
    recovered_df = pd.read_csv(
        'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_recovered_global_cleaned.csv')

    # To process confirmed cases Country and states
    listOfCountries = []
    listOfState = []
    countryStateDict = {}
    # To fetch countries and state only where the states are present
    arrangeInTwoListStateAndCountry(confirmed_df, listOfCountries, listOfState)
    deriveCountryStateListDictonary(listOfCountries, listOfState, countryStateDict)
    # To save confirmed cases Country and states to stateCountryDataForConfirmed.json
    with open(
            'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/stateCountryDataForConfirmed.json',
            'w', encoding='utf-8') as f:
        json.dump(countryStateDict, f, ensure_ascii=False, indent=4)

    # To process death related Country and states
    listOfCountries = []
    listOfState = []
    countryStateDict = {}
    # To fetch countries and state only where the states are present
    arrangeInTwoListStateAndCountry(deaths_df, listOfCountries, listOfState)
    deriveCountryStateListDictonary(listOfCountries, listOfState, countryStateDict)
    # To save death related cases Country and states to stateCountryDataForDeath.json
    with open(
            'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/stateCountryDataForDeath.json',
            'w', encoding='utf-8') as f:
        json.dump(countryStateDict, f, ensure_ascii=False, indent=4)

    # To process recovered related Country and states
    listOfCountries = []
    listOfState = []
    countryStateDict = {}
    # To fetch countries and state only where the states are present
    arrangeInTwoListStateAndCountry(recovered_df, listOfCountries, listOfState)
    deriveCountryStateListDictonary(listOfCountries, listOfState, countryStateDict)

    # To save recovered related cases Country and states to stateCountryDataForRecovered.json
    with open(
            'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/stateCountryDataForRecovered.json',
            'w', encoding='utf-8') as f:
        json.dump(countryStateDict, f, ensure_ascii=False, indent=4)


# Function to derive country and state list
def deriveCountryStateListDictonary(listOfCountries, listOfState, countryStateDict):
    tempList = []
    # This loop will run for the number of the states available
    for i in range(len(listOfState)):
        # To add first state
        if i == 0:
            tempList.append(listOfState[i])
        # To handle all other state and there index
        if i >= 1:
            if listOfCountries[i] == listOfCountries[i - 1]:
                tempList.append(listOfState[i])
                # to not miss the last country and respective states
                if i == len(listOfState) - 1:
                    countryStateDict[listOfCountries[i]] = tempList
            else:
                countryStateDict[listOfCountries[i - 1]] = tempList
                tempList = []
                tempList.append(listOfState[i])


# This method will fill countries and state only where the states are present
def arrangeInTwoListStateAndCountry(csvFile, listOfCountries, listOfState):
    for i in range(csvFile['Province/State'].size):
        # With isna we can ignore NaN values
        if not pd.isna(csvFile['Province/State'][i]):
            listOfCountries.append(csvFile['Country/Region'][i])
            listOfState.append(csvFile['Province/State'][i])


if __name__ == "__main__":
    main()
