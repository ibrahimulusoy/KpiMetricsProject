"""
KPI: TELPAS  : "% of ELs increased composite levels at least 1 level or kept the same if it is already AH
Level: Campus-level KPI
Department: Academics - ESL
KPI ID: 80800060001
Required data is in TEA web-site(https://txschools.gov/) under the " STAAR Performance Data Table" section.
https://rptsvr1.tea.texas.gov/perfreport/account/2019/download.html
Page: Data Download
Select the specified options.
1. What type of data would you like to download?
   District-level Data
   Campus-level Data
2. Select the following category of information you wish to download (select one).
    Closing the Gaps Domain
        Data Table
Download the file and save in csv file format.
Reference Page:
https://rptsvr1.tea.texas.gov/perfreport/account/2019/download/dist_d3_data.html
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'{}\CAMP_D3_DATA.csv'.format(Bases.BaseKPI.source_files_path))
df = df[['CAMPUS', 'CDLELP19R']]
dfCampuses = pd.read_csv(r'{}\Campuses.csv'.format(Bases.BaseKPI.source_files_path))
df = df.merge(dfCampuses, how='inner', left_on='CAMPUS', right_on='StateCampusCode')
df = df[['EntityID', 'CDLELP19R']]
df.rename(columns={'EntityID': 'Campus_RowID', 'CDLELP19R': 'Raw_Score'}, inplace=True)
df['Raw_Score'] = pd.to_numeric(df['Raw_Score'])
df['Raw_Score_Details'] = "TEA TAPR Advanced Data"
df['Artifact_URL'] = 'https://rptsvr1.tea.texas.gov/perfreport/account/2019/download.html'
Bases.BaseKPI.setKPIDetails(df, True, 80800060001, False)

dfDistrict = pd.read_csv(r'{}\DIST_D3_DATA.csv'.format(Bases.BaseKPI.source_files_path), low_memory=False)
dfDistrict = dfDistrict[['DISTRICT', 'DDLELP19R']]
dfCampuses = dfCampuses[dfCampuses['EntityCode'] == 0]
dfDistrict = dfDistrict.merge(dfCampuses, how='inner', left_on='DISTRICT', right_on='StateDistrictCode')
dfDistrict = dfDistrict[['DistrictID', 'DDLELP19R']]
dfDistrict.rename(columns={'DistrictID': 'DistrictKey', 'DDLELP19R': 'Raw_Score'}, inplace=True)
dfDistrict['Raw_Score'] = pd.to_numeric(dfDistrict['Raw_Score'])
dfDistrict['Raw_Score_Details'] = 'TEA TAPR Advanced Data'
dfDistrict['Artifact_URL'] = 'https://rptsvr1.tea.texas.gov/perfreport/account/2019/download.html'
Bases.BaseKPI.setDistrictKPIDetails(dfDistrict, True, 80800060001)


