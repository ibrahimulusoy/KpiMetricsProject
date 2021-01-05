'''
KPI: % of eligible educators who earned a Micro-credential
Level: Campus-level KPI
Department: Academics - Teacher Evaluation and Growth
KPI ID: 80500070001

Notes:
Download required data from BloomBoard.
% of eligible educators who earned a micro-credential during the current school year.
Pull unique MCs per educator with status [earned] during the current school year only (filter by [modified date] column)
'''

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\report_organization.csv'.format(Bases.BaseKPI.source_files_path))
df = df[(df['Schools'].str.contains('District') == 0) & (df['Schools'].str.contains('HPS') == 0) \
        & (df['Schools'].str.contains('0') == 1)]
df['Schools'] = df['Schools'].str.split(',').str[0]

dfSchools = df[['Schools']]
dfSchools = dfSchools.drop_duplicates().reset_index(drop=True)
dfSchools['TEAMSOrgID'] = dfSchools['Schools'].str.split(' - ').str[0]
dfSchools['TEAMSOrgID'] = dfSchools['TEAMSOrgID'].astype(int)
dfSchools.sort_values(by=['TEAMSOrgID'], inplace=True)
dfCampuses = pd.read_csv(r'{}\Campuses.csv'.format(Bases.BaseKPI.source_files_path))
year = dfCampuses['Description'][0].split('-')[0]
dfCampuses = dfCampuses[['EntityID', 'EntityShortName', 'TEAMSOrgID']]
dfSchools = dfSchools.merge(dfCampuses, on='TEAMSOrgID')

df = df[['Email', 'Schools', 'Status', 'Modified Date']]
df['Modified Date'] = pd.to_datetime(df['Modified Date'])
# df = df[(df['Modified Date'] > '08/01/2020') & (df['Modified Date'] < '01/01/2021')]
df = df[(df['Modified Date'] >= '08/01/{}'.format(year))]
df.drop(['Modified Date'], axis=1, inplace=True)
df = df.drop_duplicates().reset_index(drop=True)

# dfAllMC : dfAllMicroCredentials
dfAllMC = df[['Schools', 'Email']]
dfAllMC = dfAllMC.drop_duplicates().reset_index(drop=True)
dfAllMC = dfAllMC.groupby('Schools').count().reset_index()
dfAllMC.rename(columns={'Email': 'AllMC'}, inplace=True)


# dfEarnedMC : DfEarnedMicroCredentials
dfEarnedMC = df[df['Status'] == 'Earned']
dfEarnedMC = dfEarnedMC[['Schools', 'Email']]
dfEarnedMC = dfEarnedMC.drop_duplicates().reset_index(drop=True)
dfEarnedMC = dfEarnedMC.groupby('Schools').count().reset_index()
dfEarnedMC.rename(columns={'Email': 'EarnedMC'}, inplace=True)

dfProcessed = dfSchools.merge(dfAllMC, how='left', on='Schools')
dfProcessed = dfProcessed.merge(dfEarnedMC, how='left', on='Schools')
dfProcessed['EarnedMC'] = dfProcessed['EarnedMC'].fillna(0)
dfProcessed.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
dfProcessed["Raw_Score"] = dfProcessed["EarnedMC"] / dfProcessed["AllMC"] * 100
dfProcessed["Raw_Score"] = dfProcessed["Raw_Score"].fillna(0)
dfProcessed['Raw_Score_Details'] = 'Bloomboard'
dfProcessed['Artifact_URL'] = 'https://bloomboard.com/'

# dfProcessed.to_csv(r'{}\Earned_1026.csv'.format(Bases.BaseKPI.source_files_path))
Bases.BaseKPI.setKPIDetails(dfProcessed, True, 80500070001, True)
