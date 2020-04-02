"""
KPI 8: % of  Student Immunization records in file
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'C:\Users\bballiyev\OneDrive - Harmony Public Schools\Desktop\KPI Project\KPI_60800010001.csv')
df["Raw_Score"] = df["ImmunizationsIncomplete"] / df["Enrollment"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60800010001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, False, 60800010001)
print('This KPI records has been inserted to Fact_KPI_Campus table.')
print(df.to_string())
