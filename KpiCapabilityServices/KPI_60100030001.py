"""
KPI: Student Retention
"""

import pandas as pd
from BaseServices import Bases

# Get previous and current year enrolment count and calculate the score for all campuses
df = pd.read_csv(r'{}\KPI_60100030001.csv'.format(Bases.BaseKPI.source_files_path))
df["Raw_Score"] = df["TotalFinal"] / df["TotalInitial"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_60100030001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, True, 60100030001, True)

