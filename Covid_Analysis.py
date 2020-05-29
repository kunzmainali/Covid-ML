import pandas as pd

covid_file_path = ".../input/Covid-ML/us-counties.csv"
covid_data = pd.read_csv(covid_file_path)
covid_data.describe()
