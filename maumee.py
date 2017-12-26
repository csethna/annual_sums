import pandas as pd # imports Pandas datascience library as 'pd'
import os # imports os library to perform system functions such as opening files

# Specify the data source
CSV_PATH = os.path.join('maumee_annual_sums.csv')

# Create the DataFrame and reformat dates from MM/DD/YYYY to YYYY-MM-DD
df = pd.read_csv(CSV_PATH, parse_dates=['Date'], index_col=0)

# convert MM/DD/YYYY to YYY-MM-DD and save as 'dates'
#dates = pd.to_datetime(df['Date'])

# Create pivot table to focus on relevant columns
p = df.pivot_table(index=['Date'])
# Use reindex to make the 'Date' column the index column
columns = ['Maumee TP Load (tonnes)', 'Maumee SRP Load (tonnes)', 'Maumee TN Load (tonnes)', 'Maumee Silica Load (tonnes)']
p = p.reindex(columns=columns)
p[columns] = p[columns].astype(float) # assigns type to string
df = p

# Define Date Range
annual_range = df.loc['2000-1-1' : '2000-12-31']
tp_total_range = annual_range['Maumee TP Load (tonnes)'].sum()
srp_total_range = annual_range['Maumee SRP Load (tonnes)'].sum()
tn_total_range = annual_range['Maumee TN Load (tonnes)'].sum()
si_total_range = annual_range['Maumee Silica Load (tonnes)'].sum()

# Totals for Range
print("For the specified annual range: \n"
'Maumee TP Load (tonnes) = ', tp_total_range, "\n", 'Maumee SRP Load (tonnes) = ', srp_total_range, "\n", 'Maumee TN Load (tonnes) = ', tn_total_range, "\n", 'Maumee Silica Load (tonnes) = ', si_total_range)
