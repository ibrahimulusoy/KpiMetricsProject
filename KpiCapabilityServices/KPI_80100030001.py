'''
KPI: Domain I (Student Achievement) - STAAR Performance
Level: Campus-level KPI
Department: Academics
Source: The source file has been downloaded from TEA web site.
https://rptsvr1.tea.texas.gov/perfreport/account/2019/download.html
'''


import pandas as pd
from BaseServices import Bases

# Get campus-level raw scores from TEA district source file.
# We are directly downloading campus-level scale scores from TEA web site by using Selenium.
dfCampus = pd.read_csv(r'C:\Users\eatakahraman\Desktop\AcademicsKpiCampusSourceFile.csv')  # D:\UNC\KPI
dfCampus = dfCampus[['Campus_RowID', 'CD1AS']]
dfCampus.rename(columns={'CD1AS': 'Raw_Score'}, inplace=True)
dfCampus['Raw_Score_Details'] = ''
dfCampus['Artifact_URL'] = 'https://txschools.gov/schools'
Bases.BaseKPI.setKPIDetails(dfCampus, True, 80100030001, False)

# Get district-level raw scores from TEA district source file.
# We are directly downloading district-level scale scores from TEA web site by using Selenium.
dfDistrict = pd.read_csv(r'C:\Users\eatakahraman\Desktop\AcademicsKpiDistrictSourceFile.csv')  # D:\UNC\KPI
dfDistrict = dfDistrict[['DistrictKey', 'DD1AS']]
dfDistrict.rename(columns={'DD1AS': 'Raw_Score'}, inplace=True)
dfDistrict['Raw_Score_Details'] = ''
dfDistrict['Artifact_URL'] = 'https://txschools.gov/schools'
Bases.BaseKPI.setDistrictKPIDetails(dfDistrict, True, 80100030001)
