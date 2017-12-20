import pandas as pd # imports Pandas datascience library as 'pd'
import os # imports os library to perform system functions such as opening files
import datetime #imports datetime library for boolean mask

# Specify the data source
CSV_PATH = os.path.join('maumee_annual_sums.csv')
# Create the DataFrame
df = pd.read_csv(CSV_PATH)

df['Date', 'Maumee TP Load (tonnes)', 'Maumee SRP Load (tonnes)', 'Maumee TN Load (tonnes)', 'Maumee Silica Load (tonnes)']

df['Date'] = pd.to_datetime(df['Date']) # check "Date" to ensure data is a series type

start_date = df('Date')
end_date =

mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
