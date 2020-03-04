import pandas as pd
from BaseServices import Bases


df=pd.read_csv(r"C:\Users\iulusoy\Desktop\KPI\KPI_60900010001.csv")

df["Raw_Score"] = (df["DailyAbsentTotal"] / df["EnrollmentTotal"]) * 100
df["Raw_Score"] = round(df["Raw_Score"],2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60900010001'
df['Artifact_URL'] = 'SKYWARD'

print (df["Raw_Score"])

Bases.BaseKPI.setKPIDetails(df, False,60900010001)
