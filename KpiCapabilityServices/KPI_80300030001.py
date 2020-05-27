"""
KPI: NWEA MAP Growth Science
Level: Campus-level KPI
Department: Academics - MAP Growth
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\AssessmentResults.csv'.format(Bases.BaseKPI.source_files_path), low_memory=False)
df = df[['SchoolName', 'Discipline', 'GrowthMeasureYN',
         'FallToFallMetProjectedGrowth',
         'FallToWinterMetProjectedGrowth',  # has data
         'FallToSpringMetProjectedGrowth',
         'WinterToWinterMetProjectedGrowth',  # has data
         'WinterToSpringMetProjectedGrowth',
         'SpringToSpringMetProjectedGrowth']]
df = df[(df['GrowthMeasureYN'] == True) & (df['Discipline'] == 'Science')]
dfTotalSchoolStudentCounts = df.groupby('SchoolName')['FallToWinterMetProjectedGrowth'].count().reset_index()
dfTotalSchoolStudentCounts.rename(columns={'FallToWinterMetProjectedGrowth': 'TotalStudents'}, inplace=True)
dfGrowthCounts = df[(df['FallToWinterMetProjectedGrowth'] == 'Yes') | (df['FallToWinterMetProjectedGrowth'] == 'Yes*')].\
    groupby('SchoolName')['FallToWinterMetProjectedGrowth'].count().reset_index()
dfGrowthCounts.rename(columns={'FallToWinterMetProjectedGrowth': 'MadeGrowth'}, inplace=True)
df = dfGrowthCounts.merge(dfTotalSchoolStudentCounts, on='SchoolName')
df.rename(columns={'SchoolName': 'EntityShortName'}, inplace=True)
dfCampuses = pd.read_csv(r'{}\Campuses.csv'.format(Bases.BaseKPI.source_files_path))
dfCampuses = dfCampuses[['EntityID', 'EntityShortName']]
df = df.merge(dfCampuses, on='EntityShortName')
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df["Raw_Score"] = df["MadeGrowth"] / df["TotalStudents"] * 100
# df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = ''
df['Artifact_URL'] = 'https://www.nwea.org/'
Bases.BaseKPI.setKPIDetails(df, True, 80300030001, True)
