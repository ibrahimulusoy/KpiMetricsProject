
import pandas as pd
from BaseServices import Bases
# Get current and budgeted enrolment counts and calculate scores for all campuses
df1 = pd.read_excel(r"{}\HPSFS.xlsx".format(Bases.BaseKPI.source_files_path), 'FIRST Rating ')
#create dataframe
data = {'DistrictKey': ['10', '20', '30', '40','80', '70', '60'],
	'Raw_Score': [100*(df1.iat[51,2]-df1.iat[52,2])/df1.iat[51,2],100*(df1.iat[51,3]-df1.iat[52,3])/df1.iat[51,3],100*(df1.iat[51,4]-df1.iat[52,4])/df1.iat[51,4], 100*(df1.iat[51,5]-df1.iat[52,5])/df1.iat[51,5], 100*(df1.iat[51,6]-df1.iat[52,6])/df1.iat[51,6],100*(df1.iat[51,7]-df1.iat[52,7])/df1.iat[51,7],100*(df1.iat[51,8]-df1.iat[52,8])/df1.iat[51,8]]}
df_last = pd.DataFrame(data)
df_last['Raw_Score_Details'] = "Finance_Excel_Sheet"
df_last['Artifact_URL']='Finance Excel'
#print (df_last)
Bases.BaseKPI.setDistrictKPIDetails(df_last, True, 10600030001)