from EntityServices import Entities
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver

'''Useful link for gspread and oauth2client libraries :
https://medium.com/@vince.shields913/reading-google-sheets-into-a-pandas-dataframe-with-gspread-and-oauth2-375b932be7bf
'''


def startSelenium():
    chrome_options = webdriver.ChromeOptions()
    pref = {'download.default_directory': r'{}'.format(BaseKPI.source_files_path)}
    chrome_options.add_experimental_option('prefs', pref)
    browser = webdriver.Chrome(r'C:\chromedriver', options=chrome_options)
    return browser


class BaseKPI:
    # source_files_path = r'D:\UNC\KPI'
    source_files_path = r'C:\Users\eatakahraman\Desktop\KPI_UAT_Tests'

    def setKPIDetails(df, isGreaterThan, kpi_rowid, isDistrictScoresAsked):
        # Get KPI details for that specific KPI and arrange required columns for target tables
        # Insert campus-level and their district-level scores via this method.

        BaseKPI.setKPICommonColumns(df, isGreaterThan, kpi_rowid)

        if ('IsKPIApplicable' in df.columns) and (df['IsKPIApplicable'][0] == 0):
            print('The Kpi is not going to be calculated in this term.')
            return

        # Get district codes for all campuses from HPS_METRICS db.
        districts = Entities.KpiOperations.getDistrictsForAllCampuses()
        df = pd.merge(df, districts, left_on='Campus_RowID', right_on='CampusKey')
        df['CorpID'] = 1
        dfCampus = df[['CorpID', 'District_RowID', 'Campus_RowID', 'Term_RowID', 'KPI_RowID', 'Category_RowID',
                       'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight', 'Adjusted_Score', 'Score',
                       'Raw_Score', 'Raw_Score_Details', 'Artifact_URL']]

        # Delete old rows(if exists) for this KPI for this specific term before inserting new records
        Entities.KpiOperations.delKPIOldRecords(kpi_rowid, dfCampus['Term_RowID'][0])
        Entities.KpiOperations.insertFactKPICampuses(dfCampus, 'Fact_KPI_Campus')
        print('KPI {} campus-level scores has been inserted to Fact_KPI_Campus table.'.format(kpi_rowid))
        if isDistrictScoresAsked:
            BaseKPI.setCampusLevelKPIDistrictScores(df, kpi_rowid)

    def setDistrictKPIDetails(df, isGreaterThan, kpi_rowid):
        # District-level KPI scores
        # Get KPI details for that specific KPI and arrange required columns for target table
        # Target table is Fact_KPI on the HPS_METRICS db.
        BaseKPI.setKPICommonColumns(df, isGreaterThan, kpi_rowid)
        if df['isKPIApplicable'][0] == 0:
            print('The Kpi is not going to be calculated in this term.')
            return
        # max_row_id = Entities.KpiOperations.getMaxRowIdFromFactKPI()
        # max_row_id = max_row_id[''][0] + 1
        # df['RowID'] = range(max_row_id, max_row_id + len(df))
        df.rename(columns={'DistrictKey': 'District_RowID'}, inplace=True)
        df['CorpID'] = 1
        # Removed "'RowID'" column from the following line.
        df = df[['CorpID', 'Term_RowID', 'KPI_RowID', 'Category_RowID', 'Department_RowID', 'Is_KPI_Applicable',
                 'Adjusted_Weight',
                 'District_RowID', 'Adjusted_Score', 'Score', 'Raw_Score', 'Raw_Score_Details', 'Artifact_URL']]

        # Delete old rows(if exists) for this KPI for this specific term before inserting new records
        Entities.KpiOperations.delDistrictKPIOldRecords(kpi_rowid, df['Term_RowID'][0])
        Entities.KpiOperations.insertFactKPI(df, 'Fact_KPI')
        print('KPI {} district-level scores has been inserted to Fact_KPI table.'.format(kpi_rowid))

    def setCampusLevelKPIDistrictScores(df, kpi_rowid):
        # Insert district-level scores of campus-level KPIs.
        df['Raw_Score'] = df['Raw_Score'] * df['campus_weight']
        df['Score'] = df['Score'] * df['campus_weight']
        df['Adjusted_Score'] = df['Adjusted_Score'] * df['campus_weight']
        df2 = df.groupby('District_RowID').agg(TotalCampusWeight=('campus_weight', sum),
                                               Raw_Score=('Raw_Score', sum),
                                               Score=('Score', sum),
                                               Adjusted_Score=('Adjusted_Score', sum)
                                               )
        df2 = df2.reset_index()
        df2['Raw_Score'] = df2['Raw_Score'] / df2['TotalCampusWeight']
        df2['Score'] = df2['Score'] / df2['TotalCampusWeight']
        df2['Adjusted_Score'] = df2['Adjusted_Score'] / df2['TotalCampusWeight']
        df = df[['District_RowID', 'Term_RowID', 'KPI_RowID', 'Category_RowID', 'Department_RowID',
                 'Is_KPI_Applicable', 'Raw_Score_Details', 'Artifact_URL', 'Adjusted_Weight']]
        # df.drop_duplicates(keep='first', inplace=True)
        df = df.drop_duplicates()
        df = df.merge(df2, how='inner', on='District_RowID')
        df['CorpID'] = 1
        # max_row_id = Entities.KpiOperations.getMaxRowIdFromFactKPI()
        # max_row_id = max_row_id[''][0] + 1
        # df['RowID'] = range(max_row_id, max_row_id + len(df))
        # Removed "'RowID'" column from the following line.
        df = df[['CorpID', 'Term_RowID', 'KPI_RowID', 'Category_RowID', 'Department_RowID', 'Is_KPI_Applicable',
                 'Adjusted_Weight', 'District_RowID', 'Adjusted_Score', 'Score', 'Raw_Score', 'Raw_Score_Details',
                 'Artifact_URL']]
        Entities.KpiOperations.delDistrictKPIOldRecords(kpi_rowid, df['Term_RowID'][0])
        Entities.KpiOperations.insertFactKPI(df, 'Fact_KPI')
        print('KPI {} district-level scores has been inserted to Fact_KPI table.'.format(kpi_rowid))

    def setKPICommonColumns(df, isGreaterThan, kpi_rowid):
        # Get KPI details for that specific KPI and arrange required columns for target table
        kpiDetails = Entities.KpiOperations.getKPIDetails(kpi_rowid)

        if kpiDetails['Is_KPI_Applicable'][0] == 0:
            df['isKPIApplicable'] = 0
            return

        # Calculate score based on score levels on DIM_KPI_WEIGHT
        if isGreaterThan:
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
