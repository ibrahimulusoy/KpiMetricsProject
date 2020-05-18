'''
KPI: % of PBA system usage of staff members
'''

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'D:\UNC\KPI\KPI_60400090001.csv') #D:\UNC\KPI
df["Raw_Score"] = (df["EarnStaffCount"] / df["CurrentStaffCount"]) * 100
df['Raw_Score_Details'] = '[HPS_Metrics].KPI_60400090001'
df['Artifact_URL'] = 'External Reports'
Bases.BaseKPI.setKPIDetails(df, True, 60400090001)



