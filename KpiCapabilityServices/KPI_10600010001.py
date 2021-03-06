

import pandas as pd
from BaseServices import Bases
# Get current and budgeted enrolment counts and calculate scores for all campuses
df1 = pd.read_excel(r"{}\HPSFS.xlsx".format(Bases.BaseKPI.source_files_path), 'FIRST Rating ')
#create dataframe
data = {'DistrictKey': ['10', '20', '30', '40','80', '70', '60'],
	'Raw_Score': [df1.iat[238,2], df1.iat[238,3], df1.iat[238,4], df1.iat[238,5],df1.iat[238,6],df1.iat[238,7],df1.iat[238,8]]}
df_last = pd.DataFrame(data)
df_last['Raw_Score_Details'] = "Finance_Excel_Sheet"
df_last['Artifact_URL']='Finance Excel'
Bases.BaseKPI.setDistrictKPIDetails(df_last, True, 10600010001)




#df = pd.merge(df1, df2, on='EntityShortName')
#df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
#df["Raw_Score"] = df["CurrentEnrollment"] / df["BudgetedEnrollment"] * 100
#df['Raw_Score_Details'] = 'CustomDev.KPI_60100010001'
#df['Artifact_URL'] = 'SKYWARD + Budgeted Enrollment counts from Finance'
#Bases.BaseKPI.setKPIDetails(df, True, 60100010001)


