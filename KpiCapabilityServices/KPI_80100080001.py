"""
KPI: Domain III (Closing the Gaps) scale score
Level: Campus-level KPI
Department: Academics
Source: The source file has been downloaded from TEA web site.
https://rptsvr1.tea.texas.gov/perfreport/account/2019/download.html
"""


import pandas as pd
from BaseServices import Bases

# Get campus-level raw scores from TEA district source file.
# We are directly downloading campus-level scale scores from TEA web site by using Selenium.
dfCampus = pd.read_csv(r'{}\AcademicsKpiCampusSourceFile.csv'.format(Bases.BaseKPI.source_files_path))
dfCampus = dfCampus[['Campus_RowID', 'CD3S']]
dfCampus.rename(columns={'CD3S': 'Raw_Score'}, inplace=True)
dfCampus['Raw_Score_Details'] = 'TEA - Accountability Summary'
dfCampus['Artifact_URL'] = 'https://txschools.gov/schools'
Bases.BaseKPI.setKPIDetails(dfCampus, True, 80100080001, False)

# Get district-level raw scores from TEA district source file.
# We are directly downloading district-level scale scores from TEA web site by using Selenium.
dfDistrict = pd.read_csv(r'{}\AcademicsKpiDistrictSourceFile.csv'.format(Bases.BaseKPI.source_files_path))
dfDistrict = dfDistrict[['DistrictKey', 'DD3S']]
dfDistrict.rename(columns={'DD3S': 'Raw_Score'}, inplace=True)
dfDistrict['Raw_Score_Details'] = 'TEA - Accountability Summary'
dfDistrict['Artifact_URL'] = 'https://txschools.gov/schools'
Bases.BaseKPI.setDistrictKPIDetails(dfDistrict, True, 80100080001)
