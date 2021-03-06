
import pandas as pd
from BaseServices import Bases
# Get current and budgeted enrolment counts and calculate scores for all campuses
df1 = pd.read_excel(r"{}\HPSFS.xlsx".format(Bases.BaseKPI.source_files_path), 'FIRST Rating ')
#create dataframe
data = {'DistrictKey': ['10', '20', '30', '40','80', '70', '60'],
	'Raw_Score': [df1.iat[47,2], df1.iat[47,3], df1.iat[47,4], df1.iat[47,5],df1.iat[47,6],df1.iat[47,7],df1.iat[47,8]]}
df_last = pd.DataFrame(data)

df_last['Raw_Score_Details'] = "Finance_Excel_Sheet"
df_last['Artifact_URL']='Finance Excel'

#print(df_last)
Bases.BaseKPI.setDistrictKPIDetails(df_last, True, 10600050001)

