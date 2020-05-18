"""
KPI 9:  % of expulsion/withdrawal due to discipline cases
"""

import pandas as pd
from BaseServices import Bases

# Get expulsion and withdrawn student counts and calculate the score for all campuses
# D:\UNC\KPI
df = pd.read_csv(r'{}\KPI_60400070001.csv'.format(Bases.BaseKPI.source_files_path))
df["Raw_Score"] = df["Expulsion"] / df["TotalWithdrawn"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60400070001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, False, 60400070001, True)
