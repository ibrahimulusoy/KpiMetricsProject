'''
KPI: % of suspensions (OSS & P-OSS) per student enrollment
'''

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_60400080001.csv'.format(Bases.BaseKPI.source_files_path))  # D:\UNC\KPI
df = df.groupby(['EntityID', 'TotalEnrollment']).count().reset_index()
df.rename(columns={'EntityID': 'Campus_RowID', 'SuspensionCode': 'SuspensionCount'}, inplace=True)
df["Raw_Score"] = (df['SuspensionCount'] / df['TotalEnrollment']) * 100
df['Raw_Score_Details'] = 'CustomDev.KPI_60400080001'
df['Artifact_URL'] = 'SKYWARD'
Bases.BaseKPI.setKPIDetails(df, False, 60400080001, True)






