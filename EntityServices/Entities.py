import pandas as pd
from BaseServices import BaseKPI

class KpiOperations():
    global conn
    conn = BaseKPI.dbConnection()

    def insertFactKPICampuses(df: pd.DataFrame, tableName):
        df.to_sql(tableName, conn, if_exists='append', index=False)
        return

    def getKPIDetails(kpiRowID):
        sql='select k.RowID KPI_Row_Id,c.CategoryKey,w.Term_RowID,d.DepartmentKey,w.Is_KPI_Applicable,w.Weight from Dim_kpi k join Dim_Category C on  c.CategoryKey=k.CategoryKey join dim_department d on d.DepartmentKey=c.DepartmentKey join.dim_kpi_weight w on w.KPI_RowID=k.RowID where k.RowID={}'.format(kpiRowID)
        kpiDetails = pd.read_sql(sql, conn)
        return kpiDetails

    def getDistrictsForAllCampuses():
        sql='SELECT District_RowID,CampusKey FROM [HPS_METRICS_QA].[dbo].[Dim_Campus]'
        return pd.read_sql(sql, conn)

