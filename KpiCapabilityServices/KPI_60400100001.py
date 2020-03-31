'''
Manuel KPI
Department: Operations
Category: Student Safety and Discipline
KPI: # of safety committee meeting
This is a campus-level KPI
Take data to a df, sum all month columns that have a value('x' or 'X')
'''

import pandas as pd
import numpy as np
from BaseServices import Bases

df = Bases.BaseKPI.getManuelKPIData('SafetyReport', 1)
col_list = list(df)
col_list = [e for e in col_list if e not in ('EntityID', 'EntityName','')]
df[col_list] = df[col_list].replace({'x': 1, 'X': 1})
df[col_list] = np.where(df[col_list] != 1, 0, 1)
df['Raw_Score'] = (df[col_list].sum(axis=1) / len(col_list))*100
df['Raw_Score_Details'] = 'Spreadsheet check from Artifact URL'
df['Artifact_URL'] = "https://docs.google.com/spreadsheets/d/1Vch10a6fPtuAHnQmzKqOxYyFPpnb4TcWvjUUWDM5_kQ/edit?ts" \
                     "=5e7e6148#gid=0 "
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
df['Campus_RowID'] = pd.to_numeric(df['Campus_RowID'])
Bases.BaseKPI.setKPIDetails(df, True, 60400100001)







