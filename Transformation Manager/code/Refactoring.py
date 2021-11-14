import pandas as pd

def main():
    confirmed_df = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_confirmed_global_cleaned.csv')
    deaths_df = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_deaths_global_cleaned.csv')
    recovered_df = pd.read_csv('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_recovered_global_cleaned.csv')
    print(confirmed_df)
    print(deaths_df)
    print(recovered_df)
    confirmed_df.to_json('C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/JSON/test11.json')



if __name__ == "__main__":
    main()
