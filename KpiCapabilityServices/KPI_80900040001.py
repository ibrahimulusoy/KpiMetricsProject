"""
KPI: % GT students e-portfolio
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_80900040001.csv'.format(Bases.BaseKPI.source_files_path))
df["Raw_Score"] = df["GT_Students_With_ePortfolio"] / df["GT_Students_Cnt_Gr_6_12"] * 100
df["Raw_Score"] = round(df["Raw_Score"], 2)
df['Raw_Score_Details'] = 'CustomDev.KPI_80900040001'
df['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(df, True, 80900040001, True)
print('This KPI records has been inserted to Fact_KPI_Campus table.')
# print(df.to_string())