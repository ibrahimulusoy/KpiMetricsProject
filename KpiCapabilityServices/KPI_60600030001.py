"""
Operations Department's Manuel Entries
KPI: % of meal accounts over the district balance limit
This is a district-level KPI
Param1: # meal accounts over district limit
Param2: enrollment (non-CEP schools only)
"""

import pandas as pd
from BaseServices import Bases
df = Bases.BaseKPI.getManuelKPIData('OperationsKPI_FoodServices', 1)
#df.rename(columns={df.columns[2]: 'Param1', df.columns[3]: 'Param2'}, inplace=True)
df['# meal accounts over district limit'] = pd.to_numeric(df['# meal accounts over district limit'])
df['enrollment (non-CEP schools only)'] = pd.to_numeric(df['enrollment (non-CEP schools only)'])
df["Raw_Score"] = (df['# meal accounts over district limit'] / df['enrollment (non-CEP schools only)']) * 100
df['Raw_Score_Details'] = "Primero"
df['Artifact_URL'] = 'https://drive.google.com/file/d/1Zzi3WCOTCeiiivJQn5UCiPszNKWRD1pQ/view?ts=5e723e32'
Bases.BaseKPI.setDistrictKPIDetails(df, False, 60600030001)

