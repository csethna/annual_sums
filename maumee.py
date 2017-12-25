import pandas as pd # imports Pandas datascience library as 'pd'
import numpy as np
import matplotlib as plt
import os # imports os library to perform system functions such as opening files
import datetime #imports datetime library for boolean mask

# Specify the data source
CSV_PATH = os.path.join('maumee_annual_sums.csv')
# Create the DataFrame

df = df[(df['Date'] > '1/1/2000') & (df['date'] <= '1/10/2000')]

df = pd.read_csv(CSV_PATH, index_col='Date')
df['date'] = pd.date_range('1/1/2000', periods=10, freq='D')
mask = (df['date'] > '1/1/2000') & (df['date'] <= '1/8/2000')
print(df.loc[mask])

#
# df['Date', 'Maumee TP Load (tonnes)', 'Maumee SRP Load (tonnes)', 'Maumee TN Load (tonnes)', 'Maumee Silica Load (tonnes)']
#
# df['Date'] = pd.to_datetime(df['Date']) # check "Date" to ensure data is a series type
#
# start_date = df('Date')
# end_date =
#
# mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
