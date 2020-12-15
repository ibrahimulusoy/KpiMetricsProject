"""
KPI 8: % of  Student Immunization records in file
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_60800010001.csv'.format(Bases.BaseKPI.source_files_path))
df["Raw_Score"] = df["ImmunizationComplete"] / df["Enrollment"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60800010001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, False, 60800010001, True)

