"""
KPI: % of students who participated in at least one academic competition
Level: Campus-level KPI
Department: Academics - Curriculum & Assessment
KPI ID: 80400080001
External Report Name: Academic Competitions & Awards Campus Summary
"""

import pandas as pd
from BaseServices import Bases
import datetime

# CurrentDate = datetime.datetime.today().strftime('%d-%b-%Y')
# df = pd.read_excel(r'{}\AcademicCompetitions_{}.xlsx'.format(Bases.BaseKPI.source_files_path, CurrentDate))
# df.drop(df.tail(1).index, inplace=True)
# df = df[['Code', 'Participation_Student_Count', 'Enrolled_Student_Count']]
# dfCampuses = pd.read_csv(r'{}\Campuses.csv'.format(Bases.BaseKPI.source_files_path))
# dfCampuses = dfCampuses[['EntityID', 'EntityCode']]
# df = df.merge(dfCampuses, how='left', left_on='Code', right_on='EntityCode')
# df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
# df['Raw_Score'] = df["Participation_Student_Count"] / df["Enrolled_Student_Count"] * 100
# df['Raw_Score_Details'] = 'External Reports'
# df['Artifact_URL'] = 'https://skyward.harmonytx.org/ws/reports/'
# Bases.BaseKPI.setKPIDetails(df, True, 80400080001, True)


# This KPI uses same view with Academic Competitions KPI. -- HPS_Metrics.KPI_80400040001
df = pd.read_csv(r'{}\KPI_80400040001.csv'.format(Bases.BaseKPI.source_files_path))
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df['Raw_Score'] = df["Unique_Students_in_Competition"] / df["Enrollment"] * 100
df['Raw_Score_Details'] = 'HPS_Metrics.KPI_80400040001'
df['Artifact_URL'] = 'https://skyward.harmonytx.org/ws/reports/'
Bases.BaseKPI.setKPIDetails(df, True, 80400080001, True)