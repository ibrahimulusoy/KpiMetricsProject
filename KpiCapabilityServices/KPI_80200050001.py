import pandas as pd
from BaseServices import Bases


df = pd.read_csv(r"C:\Users\iulusoy\Desktop\KPI\HPSFS.xlsx")

df["Raw_Score"] = (df["EBRW_Average"])
df['Raw_Score_Details'] = 'CustomDev.KPI_80200050001'
df['Artifact_URL'] = 'SKYWARD'

print(df["Raw_Score"])

Bases.BaseKPI.setKPIDetails(df, True, 80200050001)
