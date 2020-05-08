"""
KPI: % SAT Participation - Seniors
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'C:\Users\bballiyev\OneDrive - Harmony Public Schools\Desktop\KPI Project\KPI_80200060001.csv')
df["Raw_Score"] = df["SAT Participants"] / df["Total Seniors"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_80200060001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, True, 80200060001)
print('This KPI records has been inserted to Fact_KPI_Campus table.')
print(df.to_string())