"""
KPI: % of ESL students with Meets or above in STAAR Reading
Level: Campus-level KPI
Department: Academics - ESL
KPI ID: 80800020001

Required data is in TEA web-site(https://txschools.gov/) under the " STAAR Performance Data Table" section.
https://rptsvr1.tea.texas.gov/perfreport/tapr/2019/download/DownloadData.html
Page: 2018-19 TAPR Advanced Data Download
Select the specified options.
1. What type of data would you like to download?
  Select "Campus" (For campus scores)
  Select "District" (For district scores)
2. Select the category of information you wish to download (select one).
 Select "Approaches, Meets, and Masters Grade Level (EOC, All Grades)"
Download the file and save in csv file format.

Reference Page:
https://rptsvr1.tea.texas.gov/perfreport/tapr/2019/download/campstaar2b.html
https://rptsvr1.tea.texas.gov/perfreport/tapr/2019/datadict.pdf
"""

import pandas as pd
from BaseServices import Bases

# CDL00AR01219R : % at Meets GL Standard or Above
df = pd.read_csv(r'{}\CAMPSTAAR2.csv'.format(Bases.BaseKPI.source_files_path))
df = df[['CAMPUS', 'CDL00AR01S19R']]
dfCampuses = pd.read_csv(r'{}\Campuses.csv'.format(Bases.BaseKPI.source_files_path))
df = df.merge(dfCampuses, how='inner', left_on='CAMPUS', right_on='StateCampusCode')
df = df[['EntityID', 'CDL00AR01S19R']]
df.rename(columns={'EntityID': 'Campus_RowID', 'CDL00AR01S19R': 'Raw_Score'}, inplace=True)
df['Raw_Score'] = pd.to_numeric(df['Raw_Score'])
df['Raw_Score_Details'] = "TEA TAPR Advanced Data"
df['Artifact_URL'] = 'https://rptsvr1.tea.texas.gov/perfreport/tapr/2019/download/DownloadData.html'
Bases.BaseKPI.setKPIDetails(df, True, 80800020001, False)

# Select District option on the page "TEA TAPR Advanced Data" and download required data.
# DDL00AR01219R
dfDistrict = pd.read_csv(r'{}\DISTSTAAR2.csv'.format(Bases.BaseKPI.source_files_path), low_memory=False)
dfDistrict = dfDistrict[['DISTRICT', 'DDL00AR01S19R']]
dfCampuses = dfCampuses[dfCampuses['EntityCode'] == 0]
dfDistrict = dfDistrict.merge(dfCampuses, how='inner', left_on='DISTRICT', right_on='StateDistrictCode')
dfDistrict = dfDistrict[['DistrictID', 'DDL00AR01S19R']]
dfDistrict.rename(columns={'DistrictID': 'DistrictKey', 'DDL00AR01S19R': 'Raw_Score'}, inplace=True)
dfDistrict['Raw_Score'] = pd.to_numeric(dfDistrict['Raw_Score'])
dfDistrict['Raw_Score_Details'] = 'TEA TAPR Advanced Data'
dfDistrict['Artifact_URL'] = 'https://rptsvr1.tea.texas.gov/perfreport/tapr/2019/download/DownloadData.html'
Bases.BaseKPI.setDistrictKPIDetails(dfDistrict, True, 80800020001)
