import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read csv file
cases = pd.read_csv("311_Cases.csv", sep = ",", dtype = "str")

# Drop extra columns
cases = cases.drop(cases.columns[range(20,47)], axis = 1)



####### Date Columns #####
date_columns = ["Opened", "Closed", "Updated"]

# Convert specified columns into datetime format
cases[date_columns] = cases[date_columns].apply(pd.to_datetime, format = "%m/%d/%Y %I:%M:%S %p")

# Find Closed - Opened in hours
time_elapsed = (cases["Closed"] - cases["Opened"])/np.timedelta64(1, 'h')

# Insert Time Elapsed into cases df
cases.insert(3, "Time Elapsed", time_elapsed)

cases = cases.dropna()
########


####### New Cases df with Dummies ###############
cat_name = ['Status','Category', 'Request Type', 'Responsible Agency','Street', 'Neighborhood', 'Police District']


new_cases = pd.DataFrame(cases['Time Elapsed'])

for i in cat_name:
    x = pd.get_dummies(cases[i], drop_first=True)
    new_cases = pd.concat([new_cases, x], axis = 1)

new_cases
########