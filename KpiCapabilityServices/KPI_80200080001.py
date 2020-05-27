"""
KPI: % AP Enrollment - Seniors
Level: Campus-level KPI
Department: Academics - College Bound
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_80200080001.csv'.format(Bases.BaseKPI.source_files_path))
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df["Raw_Score"] = df["SeniorAPEnrollment"] / df["SeniorEnrollment"] * 100
df['Raw_Score_Details'] = 'CustomDev.KPI_80200080001'
df['Artifact_URL'] = 'SKYWARD'
Bases.BaseKPI.setKPIDetails(df, True, 80200080001, True)





