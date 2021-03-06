import kpiconfig as cfg
import sqlalchemy
# from sqlalchemy import create_engine
import pandas as pd


# from BaseServices import BaseKPI
# from BaseServices import Bases

class KpiOperations:
    global conn

    conn = sqlalchemy.create_engine('mssql+pyodbc://{}:{}@{}/{}?driver={}'
                                    .format(cfg.mssql['Username'], cfg.mssql['Password'], cfg.mssql['Server'],
                                            cfg.mssql['Database'], cfg.mssql['Driver']))

    def getKPIDetails(KPI_RowID):
        sql = 'select k.RowID KPI_Row_Id,c.RowID CategoryKey,w.Term_RowID,d.RowID DepartmentKey, ' \
              'w.Is_KPI_Applicable,w.Weight,w.Score4,w.Score3,w.Score2,w.Score1 ' \
              'from Dim_kpi k ' \
              'join Dim_Category C on  c.CategoryKey=k.CategoryKey ' \
              'join dim_department d on d.DepartmentKey=c.DepartmentKey ' \
              'join.dim_kpi_weight w on w.KPI_RowID=k.RowID ' \
              'where k.RowID={}' \
              'and w.Term_RowID=(select max(RowID) Term_Row_ID from Dim_Term t)'.format(KPI_RowID)
        kpiDetails = pd.read_sql(sql, conn)
        return kpiDetails
    def getManualKPIsCampusData(Term_RowId):
        sql = 'SELECT c.corpid,c.term_rowid,c.kpi_rowid,c.category_rowid, c.Department_RowID,c.Is_KPI_Applicable,c.Adjusted_Weight,c.District_RowID, ISNULL(ROUND(sum(adjusted_score) / sum(adjusted_weight), 1), 0)* c.Adjusted_Weight adjusted_score,  ISNULL(ROUND(sum(adjusted_score) / sum(adjusted_weight), 1), 0) Score ' \
              'FROM dbo.Fact_KPI_Campus c ' \
              'WHERE Term_RowID = {} AND KPI_RowID IN (SELECT KPI_RowID FROM dbo.Dim_KPI_Weight w WHERE w.Term_RowID = {} AND Calculation_Type = {} ) ' \
              'GROUP BY c.corpid, c.term_rowid,c.kpi_rowid,c.category_rowid, c.Department_RowID,c.Is_KPI_Applicable,c.Adjusted_Weight,c.District_RowID '.format(Term_RowId, Term_RowId, "'M'")

        # ROUND(sum(adjusted_score) / sum(adjusted_weight), 1), 0)* c.Adjusted_Weight adjusted_score,  ISNULL(ROUND(sum(adjusted_score) / sum(adjusted_weight), 1), 0) Score '
        resultSet = pd.read_sql(sql, conn)
        return resultSet


    # def getKPIDetails(KPI_RowID):
    #     sql = 'select k.RowID KPI_Row_Id,c.CategoryKey,w.Term_RowID,d.DepartmentKey, ' \
    #           'w.Is_KPI_Applicable,w.Weight,w.Score4,w.Score3,w.Score2,w.Score1 ' \
    #           'from Dim_kpi k ' \
    #           'join Dim_Category C on  c.CategoryKey=k.CategoryKey ' \
    #           'join dim_department d on d.DepartmentKey=c.DepartmentKey ' \
    #           'join.dim_kpi_weight w on w.KPI_RowID=k.RowID ' \
    #           'where k.RowID={}' \
    #           'and w.Term_RowID=(select max(RowID) Term_Row_ID from Dim_Term t)'.format(KPI_RowID)
    #     kpiDetails = pd.read_sql(sql, conn)
    #     return kpiDetails

    def getDistrictsForAllCampuses():
        sql = 'SELECT District_RowID, CampusKey, campus_weight FROM Dim_Campus'
        return pd.read_sql(sql, conn)

    def delKPIOldRecords(KPI_RowID, Term_RowID):
        # sql='Delete [HPS_METRICS_QA].[dbo].[Fact_KPI_Campus] where KPI_RowID={} and Term_RowID={}'.format(
        # KPI_RowID, Term_RowID)
        sql = 'Delete Fact_KPI_Campus where KPI_RowID={} and Term_RowID={}'.format(KPI_RowID, Term_RowID)
        conn.execute(sql)

    def delDistrictKPIOldRecords(KPI_RowID, Term_RowID):
        sql = 'Delete Fact_KPI where KPI_RowID={} and Term_RowID={}'.format(KPI_RowID, Term_RowID)
        conn.execute(sql)

    def insertFactKPICampuses(df: pd.DataFrame, tableName):
        df.to_sql(tableName, conn, if_exists='append', index=False)

    def insertFactKPI(df: pd.DataFrame, tableName):
        df.to_sql(tableName, conn, if_exists='append', index=False)

    def getMaxRowIdFromFactKPI():
        sql = 'select max(rowid) FROM [HPS_METRICS_QA].[dbo].[Fact_KPI]'
        return pd.read_sql(sql, conn)
