'''
KPI: Domain I (Student Achievement) - CCMR
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
dfCampus = dfCampus[['Campus_RowID', 'CD1BS']]
dfCampus.rename(columns={'CD1BS': 'Raw_Score'}, inplace=True)
# dfCampus = dfCampus[dfCampus['Raw_Score'] != '.']
dfCampus.drop(dfCampus[dfCampus['Raw_Score'] == '.'].index, inplace=True)
dfCampus['Raw_Score'] = pd.to_numeric(dfCampus['Raw_Score'])
dfCampus['Raw_Score_Details'] = ''
dfCampus['Artifact_URL'] = 'https://txschools.gov/schools'
Bases.BaseKPI.setKPIDetails(dfCampus, True, 80100040001, False)

# Get district-level raw scores from TEA district source file.
# We are directly downloading district-level scale scores from TEA web site by using Selenium.
dfDistrict = pd.read_csv(r'C:\Users\eatakahraman\Desktop\AcademicsKpiDistrictSourceFile.csv')  # D:\UNC\KPI
dfDistrict = dfDistrict[['DistrictKey', 'DD1BS']]
dfDistrict.rename(columns={'DD1BS': 'Raw_Score'}, inplace=True)
dfDistrict['Raw_Score_Details'] = ''
dfDistrict['Artifact_URL'] = 'https://txschools.gov/schools'
Bases.BaseKPI.setDistrictKPIDetails(dfDistrict, True, 80100040001)
