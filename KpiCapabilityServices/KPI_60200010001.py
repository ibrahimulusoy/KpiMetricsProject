import pandas as pd
from sqlalchemy import create_engine
import kpiconfig as cfg

global conn
conn = create_engine('mssql+pyodbc://{}:{}@{}/{}?driver={}'
                     .format(cfg.mssql['Username'], cfg.mssql['Password'], cfg.mssql['Server'], cfg.mssql['Database'],
                             cfg.mssql['Driver']))


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
    sql = 'Delete [HPS_METRICS_QA].[dbo].[Fact_KPI_Campus] where KPI_RowID={} and Term_RowID={}'.format(
        KPI_RowID, Term_RowID)
    conn.execute(sql)

df=pd.read_csv(r"C:\Users\iulusoy\Desktop\KPI\KPI_60200010001.csv")

df["Division"] = df["TotalADA"] / df["TotalEnrollmentDays"] * 100
df["Score"] = df["Division"].apply(lambda x: 4 if x >= 97 else (3 if x >= 96.5 else (2 if x >= 96 else (1 if x >= 95 else 0))))

kpiDetails=getKPIDetails(60200010001)
Term_RowID = int(kpiDetails['Term_RowID'])
df['Term_RowID'] = Term_RowID
df['KPI_RowID']= int(kpiDetails['KPI_Row_Id'])
df['Category_RowID']= int(kpiDetails['CategoryKey'])
df['Department_RowID']=int(kpiDetails['DepartmentKey'])
df['Is_KPI_Applicable']=int(kpiDetails['Is_KPI_Applicable'])
adjustedWeight = int(kpiDetails['Is_KPI_Applicable']) * int(kpiDetails['Weight'])
df['Adjusted_Weight']= adjustedWeight
df['Adjusted_Score'] = df['Adjusted_Weight'] * df['Score']

districts = getDistrictsForAllCampuses()
df = pd.merge(df, districts, left_on='EntityID', right_on='CampusKey')
df["Raw_Score"] = (df["TotalADA"] / df["TotalEnrollmentDays"] )*100
df["Raw_Score_Details"] ="CustomDev.KPI_60200010001"
df["Artifact_Url"] ="SKYWARD"
df = df[['District_RowID', 'CampusKey', 'Term_RowID', 'KPI_RowID', 'Category_RowID',
         'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight', 'Adjusted_Score', 'Score', 'Raw_Score','Raw_Score_Details','Artifact_Url']]

df.rename(columns={"CampusKey": "Campus_RowID"}, inplace=True)

delKPIOldRecords(60200010001, Term_RowID)
insertFactKPICampuses(df, 'Fact_KPI_Campus')
#df.to_csv(r'C:\Users\iulusoy\Desktop\KPI\KPI.csv')



