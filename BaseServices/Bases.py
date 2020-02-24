from EntityServices import Entities
import pandas as pd


class BaseKPI():
    def setKPIDetails(df, kpi_rowid):
        # Get KPI details for that spacific KPI and arrange required columns for target table
        # Target table is Fact_KPI_Campus on the HPS_METRICS db.
        kpiDetails = Entities.KpiOperations.getKPIDetails(kpi_rowid)

        # Calculate score based on score levels on DIM_KPI_WEIGHT
        df["Score"] = df["Raw_Score"].apply(lambda x: 4 if x >= int(kpiDetails['Score4'])
                                                        else (3 if x >= int(kpiDetails['Score3'])
                                                        else (2 if x >= int(kpiDetails['Score2'])
                                                        else (1 if x >= int(kpiDetails['Score1'])
                                                        else 0))))

        Term_RowID = int(kpiDetails['Term_RowID'])
        df['Term_RowID'] = Term_RowID
        df['KPI_RowID'] = int(kpiDetails['KPI_Row_Id'])
        df['Category_RowID'] = int(kpiDetails['CategoryKey'])
        df['Department_RowID'] = int(kpiDetails['DepartmentKey'])
        df['Is_KPI_Applicable'] = int(kpiDetails['Is_KPI_Applicable'])
        adjustedWeight = int(kpiDetails['Is_KPI_Applicable']) * int(kpiDetails['Weight'])
        df['Adjusted_Weight'] = adjustedWeight
        df['Adjusted_Score'] = df['Adjusted_Weight'] * df['Score']

        # Get district codes for all campuses from HPS_METRICS db.
        districts = Entities.KpiOperations.getDistrictsForAllCampuses()
        df = pd.merge(df, districts, left_on='Campus_RowID', right_on='CampusKey')
        df = df[['District_RowID', 'Campus_RowID', 'Term_RowID', 'KPI_RowID', 'Category_RowID',
                 'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight', 'Adjusted_Score', 'Score', 'Raw_Score']]
        df['Raw_Score_Details'] = 'CustomDev.KPI_60400090001'
        df['Artifact_URL'] = 'External Reports'
        # Delete old rows(if exists) for this KPI for this specific term before inserting new records
        Entities.KpiOperations.delKPIOldRecords(kpi_rowid, Term_RowID)
        Entities.KpiOperations.insertFactKPICampuses(df, 'Fact_KPI_Campus')
        return df



