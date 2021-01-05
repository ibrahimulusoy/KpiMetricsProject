'''
KPI: Number of Enrollment
'''

import pandas as pd
from BaseServices import Bases
# Get current and budgeted enrolment counts and calculate scores for all campuses
df1 = pd.read_excel(r"{}\HPSFS.xlsx".format(Bases.BaseKPI.source_files_path), 'FIRST Rating ')
#create dataframe
data = {'DistrictKey': ['10', '20', '30', '40','80', '70', '60'],
	'Raw_Score': [df1.iat[61,2], df1.iat[61,3], df1.iat[61,4], df1.iat[61,5],df1.iat[61,6],df1.iat[61,7],df1.iat[61,8]]}
df_last = pd.DataFrame(data)

df_last['Raw_Score']=df_last['Raw_Score'].str.replace(r' Days', '')
df_last['Raw_Score']=pd.to_numeric(df_last['Raw_Score'])
df_last['Raw_Score_Details'] = "Finance_Excel_Sheet"
df_last['Artifact_URL']='Finance Excel'
Bases.BaseKPI.setDistrictKPIDetails(df_last, True, 10600040001)





