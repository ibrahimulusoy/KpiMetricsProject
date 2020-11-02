'''
% of Withdrawn student rate
'''

import pandas as pd
from BaseServices import Bases


df = pd.read_csv(r'{}\KPI_60200020001.csv'.format(Bases.BaseKPI.source_files_path))

df["Raw_Score"] = (df["TotalWithdrawn"] / df["CurrentEnrollment"]) * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60200020001'
df['Artifact_URL'] = 'SKYWARD'

# print(df["Raw_Score"])

Bases.BaseKPI.setKPIDetails(df, False, 60200020001, True)
