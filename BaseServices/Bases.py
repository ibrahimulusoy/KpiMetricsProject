from EntityServices import Entities
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
'''Useful link for gspread and oauth2client libraries :
https://medium.com/@vince.shields913/reading-google-sheets-into-a-pandas-dataframe-with-gspread-and-oauth2-375b932be7bf
'''

class BaseKPI():
    def setKPIDetails(df, isGreaterThan, kpi_rowid):
        # Get KPI details for that specific KPI and arrange required columns for target table
        # Target table is Fact_KPI_Campus on the HPS_METRICS db.
        BaseKPI.setKPICommonColumns(df, isGreaterThan, kpi_rowid)

        # Get district codes for all campuses from HPS_METRICS db.
        districts = Entities.KpiOperations.getDistrictsForAllCampuses()
        df = pd.merge(df, districts, left_on='Campus_RowID', right_on='CampusKey')
        df = df[['District_RowID', 'Campus_RowID', 'Term_RowID', 'KPI_RowID', 'Category_RowID',
                 'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight', 'Adjusted_Score', 'Score', 'Raw_Score', 'Raw_Score_Details', 'Artifact_URL']]

        # Delete old rows(if exists) for this KPI for this specific term before inserting new records
        Entities.KpiOperations.delKPIOldRecords(kpi_rowid, df['Term_RowID'][0])
        Entities.KpiOperations.insertFactKPICampuses(df, 'Fact_KPI_Campus')
        print('KPI {} records has been inserted to Fact_KPI_Campus table.'.format(kpi_rowid))

    def setDistrictKPIDetails(df, isGreaterThan, kpi_rowid):
        # Get KPI details for that specific KPI and arrange required columns for target table
        # Target table is Fact_KPI on the HPS_METRICS db.
        BaseKPI.setKPICommonColumns(df, isGreaterThan, kpi_rowid)
        max_row_id = Entities.KpiOperations.getMaxRowIdFromFactKPI()
        max_row_id = max_row_id[''][0] + 1
        df['RowID'] = range(max_row_id, max_row_id + len(df))
        df.rename(columns={'DistrictKey' : 'District_RowID'}, inplace=True)
        df = df[['RowID', 'Term_RowID', 'KPI_RowID', 'Category_RowID', 'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight',
                 'District_RowID', 'Adjusted_Score', 'Score', 'Raw_Score', 'Raw_Score_Details', 'Artifact_URL']]

        # Delete old rows(if exists) for this KPI for this specific term before inserting new records
        Entities.KpiOperations.delDistrictKPIOldRecords(kpi_rowid, df['Term_RowID'][0])
        Entities.KpiOperations.insertFactKPI(df, 'Fact_KPI')
        print('KPI {} records has been inserted to Fact_KPI_Campus table.'.format(kpi_rowid))

    def setKPICommonColumns(df, isGreaterThan, kpi_rowid):
        # Get KPI details for that specific KPI and arrange required columns for target table
        kpiDetails = Entities.KpiOperations.getKPIDetails(kpi_rowid)

        # Calculate score based on score levels on DIM_KPI_WEIGHT
        if isGreaterThan == True:
            df["Score"] = df["Raw_Score"].apply(lambda x: 4 if x >= float(kpiDetails['Score4'])
            else (3 if x >= float(kpiDetails['Score3'])
                  else (2 if x >= float(kpiDetails['Score2'])
                        else (1 if x >= float(kpiDetails['Score1'])
                              else 0))))
        else:
            df["Score"] = df["Raw_Score"].apply(lambda x: 4 if x <= int(kpiDetails['Score4'])
            else (3 if x <= float(kpiDetails['Score3'])
                  else (2 if x <= float(kpiDetails['Score2'])
                        else (1 if x <= float(kpiDetails['Score1'])
                              else 0))))

        Term_RowID = int(kpiDetails['Term_RowID'])
        df['Term_RowID'] = Term_RowID
        df['KPI_RowID'] = int(kpiDetails['KPI_Row_Id'])
        df['Category_RowID'] = int(kpiDetails['CategoryKey'])
        df['Department_RowID'] = int(kpiDetails['DepartmentKey'])
        df['Is_KPI_Applicable'] = int(kpiDetails['Is_KPI_Applicable'])
        adjustedWeight = float(kpiDetails['Is_KPI_Applicable']) * float(kpiDetails['Weight'])
        df['Adjusted_Weight'] = adjustedWeight
        df['Adjusted_Score'] = df['Adjusted_Weight'] * df['Score']
        return df

    def getManuelKPIData(sheetName, sheetIndex):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            '../KpiCapabilityServices/expanded-port-272114-843e9cf642c4.json', scope)  # Your json file here
        gc = gspread.authorize(credentials)

        wks = gc.open(sheetName).get_worksheet(sheetIndex)
        data = wks.get_all_values()
        headers = data.pop(0)
        df = pd.DataFrame(data, columns=headers)
        return df




