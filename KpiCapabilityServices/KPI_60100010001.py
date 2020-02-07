'''
KPI: Number of Enrollment
'''

import pandas as pd
from EntityServices import Entities

#Get current and budgeted enrolment count and calculate the score for all campuses
df1 = pd.read_csv(r'C:\Users\eatakahraman\Desktop\KPI_60100010001.csv')
df2 = pd.read_csv(r'C:\Users\eatakahraman\Desktop\KPI_60100010001_Budgeted.csv')
df = pd.merge(df1, df2, on='EntityShortName')
df["Division"] = df["CurrentEnrollment"] / df["BudgetedEnrollment"] * 100
df["Score"] = df["Division"].apply(lambda x: 4 if x >= 102 else (3 if x >= 100 else (2 if x >= 98 else (1 if x >= 97 else 0))))

#Get KPI details for that spacific KPI and arrange required columns for target table
#Target table is Fact_KPI_Campus on the HPS_METRICS db.
kpiDetails = Entities.KpiOperations.getKPIDetails(60100010001)
df.rename(columns={'EntityID':'Campus_RowID'}, inplace=True)
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
         'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight', 'Adjusted_Score', 'Score']]

#Delete old rows(if exists) for this KPI for this specific term before inserting new records
Entities.KpiOperations.delKPIOldRecords(60100010001, Term_RowID)
Entities.KpiOperations.insertFactKPICampuses(df, 'Fact_KPI_Campus')

