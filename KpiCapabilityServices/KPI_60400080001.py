'''
KPI: % of suspensions (OSS & P-OSS) per student enrollment
'''

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'C:\Users\eatakahraman\Desktop\KPI_60400080001.csv') #D:\UNC\KPI
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df["Raw_Score"] = (df['SuspensionCount'] / df['EntityTotalEnrollment']) * 100
df['Raw_Score_Details'] = 'CustomDev.KPI_60400080001'
df['Artifact_URL'] = 'SKYWARD'
Bases.BaseKPI.setKPIDetails(df, False, 60400080001)






