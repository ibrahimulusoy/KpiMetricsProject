"""
% Average Daily Attendance rate success rate
"""


import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'C:\Users\iulusoy\Documents\KPI\KPI_60200010001.csv'.format(Bases.BaseKPI.source_files_path))

df["Raw_Score"] = (df["TotalADA"] / df["TotalEnrollmentDays"]) * 100
df["Raw_Score"] =df["Raw_Score"].round(4)
df["Raw_Score_Details"] = "CustomDev.KPI_60200010001"
df["Artifact_URL"] = "SKYWARD"

Bases.BaseKPI.setKPIDetails(df, True, 60200010001, True)