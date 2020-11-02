"""
KPI:  % of ESL students exited the program after 5 years
Level: District-level KPI
Department: Academics - ESL
KPI ID: 80800070001
Source: Skyward
Notes: A student needs to exit ESL in five years in normal conditions. If a student stays more than 5 years in ESL,
it needs to be flagged.
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_excel(r'{}\EllevationKPI.xlsx'.format(Bases.BaseKPI.source_files_path))
print(df.columns)
dfAll = df.groupby("DistrictID").count().reset_index()
dfAll = dfAll[['DistrictID', 'StudentID']]
dfAll.rename(columns={'StudentID': 'AllESLStudents'}, inplace=True)
dfLessThenFiveYears = df[df['Diff'] <= 60]
dfLessThenFiveYears = dfLessThenFiveYears.groupby('DistrictID').count().reset_index()
dfLessThenFiveYears = dfLessThenFiveYears[['DistrictID', 'StudentID']]
dfLessThenFiveYears.rename(columns={'StudentID': 'LessThenFiveYearsESL'}, inplace=True)
dfAll = dfAll.merge(dfLessThenFiveYears, how='inner', on='DistrictID')
dfAll["Raw_Score"] = dfAll["LessThenFiveYearsESL"] / dfAll["AllESLStudents"] * 100
dfAll['Raw_Score_Details'] = ''
dfAll['Artifact_URL'] = 'SKYWARD'

dfProcessed.to_csv(r'{}\Earned_1026.csv'.format(Bases.BaseKPI.source_files_path))
# Bases.BaseKPI.setKPIDetails(dfProcessed, True, 80800070001, True)
