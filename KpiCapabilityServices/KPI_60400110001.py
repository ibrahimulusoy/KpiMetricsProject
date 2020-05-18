'''
KPI: % of RP system usage of staff members
'''

import pandas as pd
from BaseServices import Bases

df = pd.read_csv('{}\KPI_60400110001.csv'.format(Bases.BaseKPI.source_files_path))
df["Raw_Score"] = (df["RPStaffCount"] / df["CurrentStaffCount"]) * 100
df['Raw_Score_Details'] = '[HPS_Metrics].KPI_60400110001'
df['Artifact_URL'] = 'External Reports'
Bases.BaseKPI.setKPIDetails(df, True, 60400110001, True)
