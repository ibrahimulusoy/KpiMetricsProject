'''
KPI: Student Retention
'''

import pandas as pd
from EntityServices import Entities

# Get previous and current year enrolment count and calculate the score for all campuses
df = pd.read_csv('KPI_60100030001.csv')
df["Raw_Score"] = df["TotalFinal"] / df["TotalInitial"] * 100
df["Score"] = df["Raw_Score"].apply(
    lambda x: 4 if x >= 88 else (3 if x >= 82 else (2 if x >= 76 else (1 if x >= 70 else 0))))

# Get KPI details for that specific KPI and arrange required columns for target table
# Target table is Fact_KPI_Campus on the HPS_METRICS db.
kpiDetails = Entities.KpiOperations.getKPIDetails(60100030001)
df.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
Term_RowID = int(kpiDetails['Term_RowID'])
df['Term_RowID'] = Term_RowID
df['KPI_RowID'] = int(kpiDetails['KPI_Row_Id'])
df['Category_RowID'] = int(kpiDetails['CategoryKey'])
df['Department_RowID'] = int(kpiDetails['DepartmentKey'])
df['Is_KPI_Applicable'] = int(kpiDetails['Is_KPI_Applicable'])
adjustedWeight = int(kpiDetails['Is_KPI_Applicable']) * int(kpiDetails['Weight'])
df['Adjusted_Weight'] = adjustedWeight
df['Adjusted_Score'] = df['Adjusted_Weight'] * df['Score']
df['Raw_Score_Details'] = 'CustomDev.KPI_60100030001'
df['Artifact_URL'] = 'SKYWARD'

# Get district codes for all campuses from HPS_METRICS db.
districts = Entities.KpiOperations.getDistrictsForAllCampuses()
df = pd.merge(df, districts, left_on='Campus_RowID', right_on='CampusKey')
df = df[['District_RowID', 'Campus_RowID', 'Term_RowID', 'KPI_RowID', 'Category_RowID',
         'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight', 'Adjusted_Score', 'Score', 'Raw_Score',
         'Raw_Score_Details', 'Artifact_URL']]

# Delete old rows(if exists) for this KPI for this specific term before inserting new records
Entities.KpiOperations.delKPIOldRecords(60100030001, Term_RowID)
Entities.KpiOperations.insertFactKPICampuses(df, 'Fact_KPI_Campus')
