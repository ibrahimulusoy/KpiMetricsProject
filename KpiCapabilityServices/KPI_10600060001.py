

import pandas as pd
from BaseServices import Bases
# Get current and budgeted enrolment counts and calculate scores for all campuses
df1 = pd.read_excel(r"{}\HPSFS.xlsx".format(Bases.BaseKPI.source_files_path), 'FIRST Rating ')
#create dataframe
data = {'DistrictKey': ['10', '20', '30', '40','80', '70', '60'],
	'Raw_Score': [df1.iat[84,2], df1.iat[84,3], df1.iat[84,4], df1.iat[84,5],df1.iat[84,6],df1.iat[84,7],df1.iat[84,8]]}
df_last = pd.DataFrame(data)

df_last['Raw_Score_Details'] = "Finance_Excel_Sheet"
df_last['Artifact_URL']='Finance Excel'

#print(df_last)
Bases.BaseKPI.setDistrictKPIDetails(df_last,False, 10600060001)

