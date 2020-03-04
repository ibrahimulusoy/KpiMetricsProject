"""
KPI: Student Retention
"""

import pandas as pd
from BaseServices import Bases

# Get previous and current year enrolment count and calculate the score for all campuses
df = pd.read_csv(r'C:\Users\bballiyev\OneDrive - Harmony Public Schools\Desktop\KPI Project\KPI_60100030001.csv')
df["Raw_Score"] = df["TotalFinal"] / df["TotalInitial"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60100030001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, True, 60100030001)
print('This KPI records has been inserted to Fact_KPI_Campus table.')
print(df.to_string())
