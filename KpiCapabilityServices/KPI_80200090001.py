"""
KPI: % AP Passing
Level: Campus-level KPI
Department: Academics - College Bound
"""

import pandas as pd
from BaseServices import Bases

dfAPPassing = pd.read_csv(r'{}\AP Student Datafile 2019.csv'.format(Bases.BaseKPI.source_files_path))

ExamCodeColumns = []
dfAPPassing.columns.map(lambda x: ExamCodeColumns.append(x) if 'Exam Code' in x else None)
dfExams = dfAPPassing[ExamCodeColumns]
dfExams['ExamCount'] = dfExams.apply(lambda x: x.count(), axis=1)
dfExams['AICode'] = dfAPPassing['AI Code']
dfExams = dfExams[['AICode', 'ExamCount']]
dfExams = dfExams.groupby('AICode').sum().reset_index()

GradeColumns = []
dfAPPassing.columns.map(lambda x: GradeColumns.append(x) if 'Exam Grade' in x else None)
dfGrades = dfAPPassing[GradeColumns]
dfGrades['PassedExams'] = dfGrades.apply(lambda row: sum(row[:] >= 3), axis=1)
dfGrades['AICode'] = dfAPPassing['AI Code']
dfGrades = dfGrades[['AICode', 'PassedExams']]
dfGrades = dfGrades.groupby('AICode').sum().reset_index()
df = dfExams.merge(dfGrades, on='AICode')

dfCampuses = pd.read_csv(r'{}/Campuses.csv'.format(Bases.BaseKPI.source_files_path))
df = df.merge(dfCampuses, left_on='AICode', right_on='CEEB')
df = df[['EntityID', 'ExamCount', 'PassedExams']]
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df["Raw_Score"] = df["PassedExams"] / df["ExamCount"] * 100
df['Raw_Score_Details'] = ''
df['Artifact_URL'] = 'College Bound'
Bases.BaseKPI.setKPIDetails(df, True, 80200090001, True)

