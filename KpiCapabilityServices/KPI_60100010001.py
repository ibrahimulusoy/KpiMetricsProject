'''
KPI: Number of Enrollment
'''

import pandas as pd

from BaseServices import Bases

# Get current and budgeted enrolment counts and calculate scores for all campuses
df1 = pd.read_csv(r'{}\KPI_60100010001.csv'.format(Bases.BaseKPI.source_files_path))
dfCampuses = pd.read_csv(r'{}\Campuses.csv'.format(Bases.BaseKPI.source_files_path))
df1 = df1.merge(dfCampuses, on='EntityID')
df1 = df1[['EntityID', 'EntityShortName', 'CurrentEnrollment']]
df2 = pd.read_excel(r'{}\Budgeted_Enrollment.xlsx'.format(Bases.BaseKPI.source_files_path))
df = pd.merge(df1, df2, on='EntityShortName')
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df["Raw_Score"] = df["CurrentEnrollment"] / df["BudgetedEnrollment"] * 100
df['Raw_Score_Details'] = 'CustomDev.KPI_60100010001'
df['Artifact_URL'] = 'SKYWARD + Budgeted Enrollment counts from Finance'
Bases.BaseKPI.setKPIDetails(df, True, 60100010001, True)





