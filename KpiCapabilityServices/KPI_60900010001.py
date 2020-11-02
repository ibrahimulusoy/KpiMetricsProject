"""
% of student with Absences > 10%
"""

import pandas as pd
from BaseServices import Bases


df = pd.read_csv(r'{}\KPI_60900010001.csv'.format(Bases.BaseKPI.source_files_path))
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df["Raw_Score"] = (df["numberofstudents"] / df["currentenrollment"]) * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60900010001'
df['Artifact_URL'] = 'SKYWARD'
Bases.BaseKPI.setKPIDetails(df, False, 60900010001, True)



