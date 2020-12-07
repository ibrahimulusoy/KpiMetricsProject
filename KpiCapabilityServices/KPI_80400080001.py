"""
KPI: % of students who participated in at least one academic competition
Level: Campus-level KPI
Department: Academics - Curriculum & Assessment
KPI ID: 80400080001

Notes:
Selenium: AcademicCompetitions.py
Download required data from Skyward/ExternalReports.
Report Name: Academic Competitions & Awards Campus Summary
Required Column: Participation_Student_Count
Go to specified reports and download data via Selenium.
"""

import pandas as pd
from BaseServices import Bases
import datetime

CurrentDate = datetime.datetime.today().strftime('%d-%b-%Y')
df = pd.read_excel(r'{}\AcademicCompetitions_{}.xlsx'.format(Bases.BaseKPI.source_files_path, CurrentDate))
df.drop(df.tail(1).index, inplace=True)
df = df[['Code', 'Participation_Student_Count', 'Enrolled_Student_Count']]
dfCampuses = pd.read_csv(r'{}\Campuses.csv'.format(Bases.BaseKPI.source_files_path))
dfCampuses = dfCampuses[['EntityID', 'EntityCode']]
df = df.merge(dfCampuses, how='left', left_on='Code', right_on='EntityCode')
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df['Raw_Score'] = df["Participation_Student_Count"] / df["Enrolled_Student_Count"] * 100
df['Raw_Score_Details'] = 'External Reports'
df['Artifact_URL'] = 'https://skyward.harmonytx.org/ws/reports/'
Bases.BaseKPI.setKPIDetails(df, True, 80400080001, True)