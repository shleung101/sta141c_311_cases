import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

# Read csv file
cases = pd.read_csv("311_Cases.csv", sep = ",", dtype = "str")

# Drop extra columns
cases = cases.drop(cases.columns[range(20,47)], axis = 1)

####### Date Columns #####
date_columns = ["Opened", "Closed", "Updated"]

# Convert specified columns into datetime format
cases[date_columns] = cases[date_columns].apply(pd.to_datetime, format = "%m/%d/%Y %I:%M:%S %p")

# Find Closed - Opened
time_elapsed = (cases["Closed"] - cases["Opened"])

# Insert Time Elapsed into cases df
cases.insert(3, "Time Elapsed", time_elapsed)
########