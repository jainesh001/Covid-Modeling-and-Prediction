import pandas as pd
import numpy as num
import json
import csv

def main():
    header=['Country/Region', 'Lat', 'Long', 'Total_cases', 'Total_deaths', 'Total_recovered']
    f = open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/Master.json')
    data = json.load(f)

    listA=[]
    print (data['country'][0]['name'])
    for i in range(len(data['country'])):
        listB = []
        listB.append(data['country'][i]['name'])
        listB.append(data['country'][i]['Lat'])
        listB.append(data['country'][i]['Long'])
        stList=data['country'][i]['stateData']
        for j in range(len(stList)):
            dictA=stList[j]
            dateList=dictA['data']
            listB.append(dateList[-1]['confirmed'])
            listB.append(dateList[-1]['deaths'])
            listB.append(dateList[560]['recovered'])

        listA.append(listB)

    for i in range(len(listA)):
        print(listA[i])

    print(listA)

    with open('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/CumulativeCases.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(listA)


if __name__ == "__main__":
    main()
