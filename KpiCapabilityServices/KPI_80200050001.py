"""
SAT EBRW Average
"""

import pandas as pd
from BaseServices import Bases


df = pd.read_csv(r'{}\KPI_80200050001.csv'.format(Bases.BaseKPI.source_files_path))

df["Raw_Score"] = (df["EBRW_Average"])
df['Raw_Score_Details'] = 'CustomDev.KPI_80200050001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, True, 80200050001, True)
