"""
KPI: % College Ready - Seniors
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_30600010001.csv'.format(Bases.BaseKPI.source_files_path))
df["Raw_Score"] = df["College Ready"] / df["Total Seniors"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_30600010001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, True, 30600010001, True)
