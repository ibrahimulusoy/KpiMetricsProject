"""
KPI: Average # of teachers with approved PBL submissions per secondary campus
Level: Campus-level KPI
Department: Programs - Advanced Programs - STEM, GT, and PBL
KPI ID: 80900060001
"""


import pandas as pd
from BaseServices import Bases

# approved/6-12 student count
df = pd.read_csv(r'{}\KPI_80900060001.csv'.format(Bases.BaseKPI.source_files_path))
df["ApprovedTeacherCount"].fillna(0, inplace=True)
df["Raw_Score"] = df["ApprovedTeacherCount"] / df["TotalEnrollment"] * 100
df['Raw_Score_Details'] = 'HPS_Metrics.KPI_80900060001'
df['Artifact_URL'] = 'External Reports'
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
Bases.BaseKPI.setKPIDetails(df, True, 80900060001, True)


