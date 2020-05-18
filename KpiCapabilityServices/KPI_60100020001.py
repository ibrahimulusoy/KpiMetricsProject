'''
KPI: Number of Re-Enrollment
'''

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_60100020001.csv'.format(Bases.BaseKPI.source_files_path))  # D:\UNC\KPI
df["Raw_Score"] = df["Raw_Score"].map(lambda x: x[0:-1])
df["Raw_Score"] = pd.to_numeric(df["Raw_Score"])
df['Raw_Score_Details'] = 'CustomDev.KPI_60100020001'
df['Artifact_URL'] = 'SKYWARD'
Bases.BaseKPI.setKPIDetails(df, True, 60100020001, True)
