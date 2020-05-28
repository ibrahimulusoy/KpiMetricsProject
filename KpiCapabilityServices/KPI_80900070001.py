"""
KPI: % Industry Certification
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_80900070001.csv'.format(Bases.BaseKPI.source_files_path))
df["Raw_Score"] = df["Industry Certification"] / df["Total Seniors"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_80900070001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, True, 80900070001, False)
print('This KPI records has been inserted to Fact_KPI_Campus table.')
print(df.to_string())