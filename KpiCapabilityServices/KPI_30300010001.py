"""
KPI: HPS PATH - % of Visited Students (All)
Level: Campus-level KPI
Department: College & Career - Family Engagement
KPI ID: 30300010001
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_30300010001.csv'.format(Bases.BaseKPI.source_files_path))
df["Raw_Score"] = df["Perc_Students_Visited"] * 100
df['Raw_Score_Details'] = 'HPS_Metrics.KPI_30300010001'
df['Artifact_URL'] = 'External Reports'
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
Bases.BaseKPI.setKPIDetails(df, True, 30300010001, True)