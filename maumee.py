import pandas as pd # imports Pandas datascience library as 'pd'
import numpy as np
import matplotlib as plt
import os # imports os library to perform system functions such as opening files
from datetime import datetime, date #imports datetime library for boolean mask
import tabulate as tabulate

# Specify the data source
CSV_PATH = os.path.join('maumee_annual_sums.csv')

# Create the DataFrame and reformat dates from MM/DD/YYYY to YYYY-MM-DD
df = pd.read_csv(CSV_PATH, parse_dates=['Date'], index_col=0)

# convert MM/DD/YYYY to YYY-MM-DD and save as 'dates'
#dates = pd.to_datetime(df['Date'])

# Create pivot table to focus on relevant columns
p = df.pivot_table(index=['Date'])
# Use reindex to make the 'Date' column the index column
columns = ['Date', 'Maumee TP Load (tonnes)', 'Maumee SRP Load (tonnes)', 'Maumee TN Load (tonnes)', 'Maumee Silica Load (tonnes)']
p = p.reindex(columns=columns)
p[columns] = p[columns].astype(str) # assigns type to string
df = p

# Delete the empty date column
del df['Date']

# convert values to float64
df['Maumee TP Load (tonnes)'] = df['Maumee TP Load (tonnes)'].astype(str).astype(float)
df['Maumee SRP Load (tonnes)'] = df['Maumee SRP Load (tonnes)'].astype(str).astype(float)
df['Maumee TN Load (tonnes)'] = df['Maumee TN Load (tonnes)'].astype(str).astype(float)
df['Maumee Silica Load (tonnes)'] = df['Maumee Silica Load (tonnes)'].astype(str).astype(float)

YEAR_2000 = df.loc['2000-1-1' : '2000-12-31']
tp_total_2000 = YEAR_2000['Maumee TP Load (tonnes)'].sum()
srp_total_2000 = df.loc['2000-1-1' : '2000-12-31'].groupby(pd.TimeGrouper('Maumee SRP Load (tonnes)')).sum()
tn_total_2000
si_total_2000

# CORRECT WAY TO sum
df['Maumee TP Load (tonnes)'].sum()

print(df.loc['2000-6-1':'2000-6-10'])

# pretty print DataFrame
print(tabulate(df, headers='keys', tablefmt='psql'))

#
# df['Date', 'Maumee TP Load (tonnes)', 'Maumee SRP Load (tonnes)', 'Maumee TN Load (tonnes)', 'Maumee Silica Load (tonnes)']
#
# df['Date'] = pd.to_datetime(df['Date']) # check "Date" to ensure data is a series type
#
# start_date = df('Date')
# end_date =
#
# mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
