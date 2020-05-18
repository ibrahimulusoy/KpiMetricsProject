import pandas as pd
from BaseServices import Bases


df = pd.read_csv(r'{}\KPI_60900010001.csv'.format(Bases.BaseKPI.source_files_path))

df["Raw_Score"] = (df["DailyAbsentTotal"] / df["EnrollmentTotal"]) * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60900010001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, False, 60900010001, True)
