"""
KPI: G/T student retention rate
Level: Campus-level KPI
Department: Programs - Advanced Programs - STEM, GT, and PBL
KPI ID: 80900090001
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_80900090001.csv'.format(Bases.BaseKPI.source_files_path))
df['Retention'] = df['TotalFinal'] / df['TotalInitial'] * 100
df['GTRetention'] = df['GTTotalFinal'] / df['GTTotalInitial'] * 100
df['Raw_Score'] = df['GTRetention'] - df['Retention']
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df['Raw_Score_Details'] = 'CustomDev.KPI_SP_80900090001'
df['Artifact_URL'] = 'SKYWARD'
df.dropna(axis=0, subset=['Raw_Score'], inplace=True)
Bases.BaseKPI.setKPIDetails(df, True, 80900090001, True)