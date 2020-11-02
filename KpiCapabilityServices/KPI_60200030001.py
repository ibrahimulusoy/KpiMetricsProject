'''
KPI: % of withdrawn students located
'''

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_60100010001.csv'.format(Bases.BaseKPI.source_files_path))
df2 = pd.read_csv(r'{}\KPI_60200030001.csv'.format(Bases.BaseKPI.source_files_path))
df = df.merge(df2, on='EntityID', how='left')
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df['FatalErrorCount'].fillna(0, inplace=True)
df["Raw_Score"] = ((df['CurrentEnrollment'] - df['FatalErrorCount'])/df['CurrentEnrollment'])*100
df['Raw_Score_Details'] = 'CustomDev.KPI_SP_60200030001'
df['Artifact_URL'] = 'SKYWARD'
Bases.BaseKPI.setKPIDetails(df, True, 60200030001, True)

