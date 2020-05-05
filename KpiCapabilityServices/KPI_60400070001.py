"""
KPI 9:  % of expulsion/withdrawal due to discipline cases
"""

import pandas as pd
from BaseServices import Bases

# Get expulsion and withdrawn student counts and calculate the score for all campuses
# D:\UNC\KPI
df = pd.read_csv(r'C:\Users\bballiyev\OneDrive - Harmony Public Schools\Desktop\KPI Project\KPI_60400070001.csv')
df["Raw_Score"] = df["Expulsion"] / df["TotalWithdrawn"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60400070001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, False, 60400070001)
print('This KPI records has been inserted to Fact_KPI_Campus table.')
print(df.to_string())