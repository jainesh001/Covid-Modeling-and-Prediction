import pandas as pd
import numpy as num
import json
import csv


def main():
    # Defining a header list to set header in csv for later purpose
    header = ['Country/Region', 'Lat', 'Long', 'Total_cases', 'Total_deaths', 'Total_recovered']
    # Load the master json where the data needs to be extracted
    f = open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/Master.json')
    data = json.load(f)

    csvAllRowDataList = []
    # Interate for all the country in Master Data
    for i in range(len(data['country'])):
        csvIndividualRowDataList = []
        csvIndividualRowDataList.append(data['country'][i]['name'])
        csvIndividualRowDataList.append(data['country'][i]['Lat'])
        csvIndividualRowDataList.append(data['country'][i]['Long'])
        # To load stList from stateData
        stList = data['country'][i]['stateData']
        for j in range(len(stList)):
            # using temp dictA to go into further structure
            dictA = stList[j]
            dateList = dictA['data']
            csvIndividualRowDataList.append(dateList[-1]['confirmed'])
            csvIndividualRowDataList.append(dateList[-1]['deaths'])
            csvIndividualRowDataList.append(dateList[560]['recovered'])

        csvAllRowDataList.append(csvIndividualRowDataList)

    # Verifying the result
    for i in range(len(csvAllRowDataList)):
        print(csvAllRowDataList[i])

    # Write the data into csv file
    with open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Output/CumulativeCases.csv', 'w',
              encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows 2 dimension list(list inside list)
        writer.writerows(csvAllRowDataList)


if __name__ == "__main__":
    main()
