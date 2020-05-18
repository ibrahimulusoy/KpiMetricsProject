import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\KPI_60200010001.csv'.format(Bases.BaseKPI.source_files_path))

df["Raw_Score"] = (df["TotalADA"] / df["TotalEnrollmentDays"]) * 100
df["Raw_Score_Details"] = "CustomDev.KPI_60200010001"
df["Artifact_Url"] = "SKYWARD"
# df = df[['District_RowID', 'CampusKey', 'Term_RowID', 'KPI_RowID', 'Category_RowID',
#          'Department_RowID', 'Is_KPI_Applicable', 'Adjusted_Weight', 'Adjusted_Score', 'Score', 'Raw_Score','Raw_Score_Details','Artifact_Url']]

#df.rename(columns={"CampusKey": "Campus_RowID"}, inplace=True)

# delKPIOldRecords(60200010001, Term_RowID)
# insertFactKPICampuses(df, 'Fact_KPI_Campus')
#df.to_csv(r'C:\Users\iulusoy\Desktop\KPI\KPI.csv')

Bases.BaseKPI.setKPIDetails(df, True, 60200010001, True)