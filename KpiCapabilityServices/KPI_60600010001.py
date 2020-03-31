'''
Operations Department's Manuel Entries
KPI: % of Free-reduced information collection
This is a district-level KPI
Param1: # with no established eligibility
Param2: Enrollment
'''

import pandas as pd
from BaseServices import Bases

df = Bases.BaseKPI.getManuelKPIData('OperationsKPI_FoodServices', 0)
df.rename(columns={df.columns[2]: 'Param1', df.columns[3]: 'Param2'}, inplace=True)
df['Param1'] = pd.to_numeric(df['Param1'])
df['Param2'] = pd.to_numeric(df['Param2'])
df["Raw_Score"] = (df['Param2'] - df['Param1'])/df['Param2']*100
df['Raw_Score_Details'] = "Primero"
df['Artifact_URL'] = 'https://drive.google.com/file/d/1Zzi3WCOTCeiiivJQn5UCiPszNKWRD1pQ/view?ts=5e723e32'
Bases.BaseKPI.setDistrictKPIDetails(df, True, 60600010001)





