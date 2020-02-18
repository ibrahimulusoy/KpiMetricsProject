'''
KPI: Number of Re-Enrollment
'''

import pandas as pd
from EntityServices import Entities

#Get current and budgeted enrolment count and calculate the score for all campuses
df = pd.read_csv(r'C:\Users\eatakahraman\Desktop\KPI_60100020001.csv') #D:\UNC\KPI
df["Raw_Score"] = df["Raw_Score"].map(lambda x : x[0:-1])
df["Raw_Score"] = pd.to_numeric(df["Raw_Score"])
df["Score"] = df["Raw_Score"].apply(lambda x: 4 if x >= 98 else (3 if x >= 96 else (2 if x >= 95 else (1 if x >= 94 else 0))))

df.to_csv(r'C:\Users\eatakahraman\Desktop\aa.csv')

#Get KPI details for that spacific KPI and arrange required columns for target table
#Target table is Fact_KPI_Campus on the HPS_METRICS db.
kpiDetails = Entities.KpiOperations.getKPIDetails(60100020001)
Term_RowID = int(kpiDetails['Term_RowID'])
df['Term_RowID'] = Term_RowID
df['KPI_RowID']= int(kpiDetails['KPI_Row_Id'])
df['Category_RowID']= int(kpiDetails['CategoryKey'])
df['Department_RowID']=int(kpiDetails['DepartmentKey'])
df['Is_KPI_Applicable']=int(kpiDetails['Is_KPI_Applicable'])
adjustedWeight = int(kpiDetails['Is_KPI_Applicable']) * int(kpiDetails['Weight'])
df['Adjusted_Weight']= adjustedWeight
df['Adjusted_Score'] = df['Adjusted_Weight'] * df['Score']

#Get district codes for all campuses from HPS_METRICS db.
districts = Entities.KpiOperations.getDistrictsForAllCampuses()
df = pd.merge(df, districts, left_on='Campus_RowID', right_on='CampusKey')
df = df[['District_RowID', 'Campus_RowID', 'Term_RowID', 'KPI_RowID', 'Category_RowID',
         'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight', 'Adjusted_Score', 'Score', 'Raw_Score']]
df['Raw_Score_Details'] = 'CustomDev.KPI_60100020001'
df['Artifact_URL'] = 'SKYWARD'

#Delete old rows(if exists) for this KPI for this specific term before inserting new records
Entities.KpiOperations.delKPIOldRecords(60100020001, Term_RowID)
Entities.KpiOperations.insertFactKPICampuses(df, 'Fact_KPI_Campus')
print('This KPI records has been inserted to Fact_KPI_Campus table.')

