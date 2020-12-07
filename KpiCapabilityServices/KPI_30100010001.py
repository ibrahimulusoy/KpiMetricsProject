"""
KPI: Student Clubs and Athletics - % Student Participation
Level: Campus-level KPI
Department: College & Career - Student Engagement
KPI ID: 30100010001
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_30100010001.csv'.format(Bases.BaseKPI.source_files_path))
df["ClubEnrollment"].fillna(0, inplace=True)
df["Raw_Score"] = df["ClubEnrollment"] / df['TotalEnrollment'] * 100
df['Raw_Score_Details'] = 'CustomDev.KPI_30100010001'
df['Artifact_URL'] = 'Skyward'
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
Bases.BaseKPI.setKPIDetails(df, True, 30100010001, True)
