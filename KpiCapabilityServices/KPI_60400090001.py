'''
KPI: % of RP/PBA system usage of staff members
'''

import pandas as pd
from BaseServices import Bases

#Get current and budgeted enrolment count and calculate the score for all campuses
df = pd.read_csv(r'C:\Users\eatakahraman\Desktop\KPI_60400090001.csv') #D:\UNC\KPI
df["Raw_Score"] = df["EarnStaffCount"] / df["CurrentStaffCount"] * 100

Bases.BaseKPI.setKPIDetails(df, 60400090001)
print('This KPI records has been inserted to Fact_KPI_Campus table.')



