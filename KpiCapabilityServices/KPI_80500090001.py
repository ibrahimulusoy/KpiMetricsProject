'''
KPI:  % of eligible active educators who earned a micro-credential during their career
Level: Campus-level KPI
Department: Academics - Teacher Evaluation and Growth
KPI ID: 80500090001

Notes:
Download required data from BloomBoard.
 % of eligible active educators who earned a micro-credential during their career
For educators with active licenses, pull unique MCs with status [earned] regardless of when they earned it
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
dfCampuses = dfCampuses[['EntityID', 'EntityShortName', 'TEAMSOrgID']]
dfSchools = dfSchools.merge(dfCampuses, on='TEAMSOrgID')

df = df[['Email', 'Schools', 'Status', 'Micro-credential']]
df = df.drop_duplicates().reset_index(drop=True)

# dfAllMC : dfEarnedAllMicro-credentials
dfAllMC = df.groupby('Schools').count().reset_index()
# dfAllMC = dfAllMC[['Schools', 'Micro-credential']]
dfAllMC = dfAllMC[['Schools', 'Email']]
dfAllMC.rename(columns={'Email': 'Micro-credential'}, inplace=True)

# dfEarnedAllMC : DfSubmittedMicroCredentials
dfEarnedAllMC = df[df['Status'] == 'Earned']
dfEarnedAllMC = dfEarnedAllMC.groupby('Schools').count().reset_index()
dfEarnedAllMC = dfEarnedAllMC[['Schools', 'Micro-credential']]
dfEarnedAllMC.rename(columns={'Micro-credential': 'EarnedAllMC'}, inplace=True)

dfProcessed = dfSchools.merge(dfAllMC, how='left', on='Schools')
dfProcessed = dfProcessed.merge(dfEarnedAllMC, how='left', on='Schools')
dfProcessed['EarnedAllMC'] = dfProcessed['EarnedAllMC'].fillna(0)
dfProcessed.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
dfProcessed["Raw_Score"] = dfProcessed["EarnedAllMC"] / dfProcessed["Micro-credential"] * 100
dfProcessed["Raw_Score"] = dfProcessed["Raw_Score"].fillna(0)
dfProcessed['Raw_Score_Details'] = 'Bloomboard'
dfProcessed['Artifact_URL'] = 'https://bloomboard.com/'

Bases.BaseKPI.setKPIDetails(dfProcessed, True, 80500090001, True)
