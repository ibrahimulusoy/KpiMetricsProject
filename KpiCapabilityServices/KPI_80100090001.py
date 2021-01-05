'''
KPI: Average number of distinctions earned by campuses
Level: Campus-level KPI
Department: Academics
Source: The source file has been downloaded from TEA web site.
https://rptsvr1.tea.texas.gov/perfreport/account/2019/download.html
'''


import pandas as pd
import numpy as np
from BaseServices import Bases

# Get campus-level raw scores from TEA district source file.
# We are directly downloading campus-level scale scores from TEA web site by using Selenium.
dfCampus = pd.read_csv(r'{}\AcademicsKpiCampusSourceFile.csv'.format(Bases.BaseKPI.source_files_path))
col_list = ['CAD_MATH', 'CAD_POST', 'CAD_READ', 'CAD_SCIE', 'CAD_SOCI', 'CAD_GAP', 'CAD_PROGRESS']
dfCampus['CAD_SOCI'] = np.where((dfCampus['CAD_SOCI'] != '1') & (dfCampus['CAD_SOCI'] != '0'), None, dfCampus['CAD_SOCI'])
dfCampus['CAD_SOCI'] = pd.to_numeric(dfCampus['CAD_SOCI'], errors='coerce')
dfCampus['Distinct_Sum'] = dfCampus[col_list].sum(axis=1)
dfCampus['Denominator'] = np.where((dfCampus['CAD_SOCI'] != 1.0) & (dfCampus['CAD_SOCI'] != 0.0), 6, 7)
dfCampus['Raw_Score'] = dfCampus['Distinct_Sum'] * 100 / dfCampus['Denominator']
dfDistrictAvg = dfCampus[['DISTRICT', 'Distinct_Sum', 'Denominator']]
dfCampus = dfCampus[['Campus_RowID', 'Raw_Score']]
dfCampus['Raw_Score_Details'] = 'TEA - Accountability Summary'
dfCampus['Artifact_URL'] = 'https://txschools.gov/schools'
Bases.BaseKPI.setKPIDetails(dfCampus, True, 80100090001, False)

# Get district-level raw scores from TEA district source file.
# We are directly downloading district-level scale scores from TEA web site by using Selenium.
dfDistrictAvg = dfDistrictAvg.groupby('DISTRICT').agg({'Distinct_Sum': 'mean', 'Denominator': 'mean'}).reset_index()
dfDistrict = pd.read_csv(r'{}\AcademicsKpiDistrictSourceFile.csv'.format(Bases.BaseKPI.source_files_path))
dfDistrict = pd.merge(dfDistrict, dfDistrictAvg, left_on='StateDistrictCode', right_on='DISTRICT')
dfDistrict['Distinct_Sum'] = dfDistrict['Distinct_Sum'] + dfDistrict['DAD_POST']
dfDistrict['Raw_Score'] = dfDistrict['Distinct_Sum'] * 100 / dfDistrict['Denominator']
dfDistrict = dfDistrict[['DistrictKey', 'Raw_Score']]
dfDistrict['Raw_Score_Details'] = 'TEA - Accountability Summary'
dfDistrict['Artifact_URL'] = 'https://txschools.gov/schools'
Bases.BaseKPI.setDistrictKPIDetails(dfDistrict, True, 80100090001)
