'''
KPI: Student Retention
'''

import pandas as pd
from sqlalchemy import create_engine
import kpiconfig as cfg

conn = create_engine('mssql+pyodbc://{}:{}@{}/{}?driver={}'
                           .format(cfg.mssql['Username'], cfg.mssql['Password'], cfg.mssql['Server'], cfg.mssql['Database'], cfg.mssql['Driver']))

def insertFactKPICampuses(df: pd.DataFrame, tableName):
    df.to_sql(tableName, conn, if_exists='append', index=False)

def getKPIDetails(KPI_RowID):
    sql = 'select k.RowID KPI_Row_Id,c.CategoryKey,w.Term_RowID,d.DepartmentKey,w.Is_KPI_Applicable,w.Weight ' \
          'from Dim_kpi k ' \
          'join Dim_Category C on  c.CategoryKey=k.CategoryKey ' \
          'join dim_department d on d.DepartmentKey=c.DepartmentKey ' \
          'join.dim_kpi_weight w on w.KPI_RowID=k.RowID ' \
          'where k.RowID={}'.format(KPI_RowID)
    kpiDetails = pd.read_sql(sql, conn)
    return kpiDetails

def getDistrictsForAllCampuses():
    sql = 'SELECT District_RowID,CampusKey FROM [HPS_METRICS_QA].[dbo].[Dim_Campus]'
    return pd.read_sql(sql, conn)

def delKPIOldRecords(KPI_RowID, Term_RowID):
    sql = 'Delete [HPS_METRICS_QA].[dbo].[Fact_KPI_Campus] where KPI_RowID={} and Term_RowID={}'.format(KPI_RowID, Term_RowID)
    conn.execute(sql)

# Get previous and current year enrolment count and calculate the score for all campuses
df = pd.read_csv('KPI_60100030001.csv')
df["Raw_Score"] = df["TotalFinal"] / df["TotalInitial"] * 100
df["Score"] = df["Raw_Score"].apply(
    lambda x: 4 if x >= 88 else (3 if x >= 82 else (2 if x >= 76 else (1 if x >= 70 else 0))))

# Get KPI details for that specific KPI and arrange required columns for target table
# Target table is Fact_KPI_Campus on the HPS_METRICS db.
kpiDetails = getKPIDetails(60100030001)
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
districts = getDistrictsForAllCampuses()
df = pd.merge(df, districts, left_on='Campus_RowID', right_on='CampusKey')
df = df[['District_RowID', 'Campus_RowID', 'Term_RowID', 'KPI_RowID', 'Category_RowID',
         'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight', 'Adjusted_Score', 'Score', 'Raw_Score',
         'Raw_Score_Details', 'Artifact_URL']]

# Delete old rows(if exists) for this KPI for this specific term before inserting new records
delKPIOldRecords(60100030001, Term_RowID)
insertFactKPICampuses(df, 'Fact_KPI_Campus')
