'''
KPI: % of PBA system usage of staff members
'''

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_81200030001.csv'.format(Bases.BaseKPI.source_files_path)) #D:\UNC\KPI
df["Raw_Score"] = (df["EarnStaffCount"] / df["CurrentStaffCount"]) * 100
df['Raw_Score_Details'] = '[HPS_Metrics].KPI_81200030001'
df['Artifact_URL'] = 'External Reports'
Bases.BaseKPI.setKPIDetails(df, True, 81200030001, True)



