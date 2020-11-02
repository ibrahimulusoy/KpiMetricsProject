'''
KPI: Number of Enrollment
'''

import pandas as pd
from BaseServices import Bases
# Get current and budgeted enrolment counts and calculate scores for all campuses
df1 = pd.read_excel(r"C:\Users\iulusoy\Desktop\KPI\HPSFS.xlsx",'FIRST Rating ')
#create dataframe
data = {'DistrictKey': ['10', '20', '30', '40','80', '70', '60'],
	'Raw_Score': [100*(df1.iat[56,2])/df1.iat[51,2],100*(df1.iat[56,3])/df1.iat[51,3],100*(df1.iat[56,4])/df1.iat[51,4], 100*(df1.iat[56,5])/df1.iat[51,5], 100*(df1.iat[56,6])/df1.iat[51,6],100*(df1.iat[56,7])/df1.iat[51,7],100*(df1.iat[56,8])/df1.iat[51,8]]}
df_last = pd.DataFrame(data)
df_last['Raw_Score_Details'] = "Finance_Excel_Sheet"
df_last['Artifact_URL']='Finance Excel'
#print (df_last)
Bases.BaseKPI.setDistrictKPIDetails(df_last, True, 10600090001)
