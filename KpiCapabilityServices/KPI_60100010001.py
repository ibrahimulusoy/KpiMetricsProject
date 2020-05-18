'''
KPI: Number of Enrollment
'''

import pandas as pd
from BaseServices import Bases

# Get current and budgeted enrolment counts and calculate scores for all campuses
df1 = pd.read_csv(r'D:\UNC\KPI\KPI_60100010001.csv')  # C:\Users\eatakahraman\Desktop
df2 = pd.read_csv(r'D:\UNC\KPI\KPI_60100010001_Budgeted.csv')
df = pd.merge(df1, df2, on='EntityShortName')
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df["Raw_Score"] = df["CurrentEnrollment"] / df["BudgetedEnrollment"] * 100
df['Raw_Score_Details'] = 'CustomDev.KPI_60100010001'
df['Artifact_URL'] = 'SKYWARD + Budgeted Enrollment counts from Finance'
Bases.BaseKPI.setKPIDetails(df, True, 60100010001)





