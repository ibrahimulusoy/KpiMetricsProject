import pandas as pd
from BaseServices import Bases


df = pd.read_csv(r'{}\KPI_80200040001.csv'.format(Bases.BaseKPI.source_files_path))

df["Raw_Score"] = (df["Math_Average"])
df['Raw_Score_Details'] = 'CustomDev.KPI_80200040001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, True, 80200040001, True)
