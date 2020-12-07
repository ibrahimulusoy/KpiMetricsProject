"""
KPI: Number of academic competitions
Level: Campus-level KPI
Department: Academics - Curriculum & Assessment
KPI ID: 80400040001

Notes:
Selenium: AcademicCompetitions.py
Download required data from Skyward/ExternalReports.
Report Name: Academic Competitions & Awards Campus Summary
Required Column : No_of_Competitions
Go to specified reports and download data via Selenium.
"""

import pandas as pd
from BaseServices import Bases
import datetime

CurrentDate = datetime.datetime.today().strftime('%d-%b-%Y')
df = pd.read_excel(r'{}\AcademicCompetitions_{}.xlsx'.format(Bases.BaseKPI.source_files_path, CurrentDate))
df.drop(df.tail(1).index, inplace=True)
df = df[['Code', 'No_of_Competitions']]
dfCampuses = pd.read_csv(r'{}\Campuses.csv'.format(Bases.BaseKPI.source_files_path))
dfCampuses = dfCampuses[['EntityID', 'EntityCode']]
df = df.merge(dfCampuses, how='left', left_on='Code', right_on='EntityCode')
df.rename(columns={'EntityID': 'Campus_RowID', 'No_of_Competitions': 'Raw_Score'}, inplace=True)
df['Raw_Score_Details'] = 'External Reports'
df['Artifact_URL'] = 'https://skyward.harmonytx.org/ws/reports/'
Bases.BaseKPI.setKPIDetails(df, True, 80400040001, True)

