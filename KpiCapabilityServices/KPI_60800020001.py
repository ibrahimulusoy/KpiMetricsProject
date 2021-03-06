"""
KPI 7: % of Screenings complete (vision, hearing, spinal, and diabetes)
"""

import pandas as pd
from BaseServices import Bases
from EntityServices import Entities
from datetime import datetime
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv(r'{}\KPI_60800020001.csv'.format(Bases.BaseKPI.source_files_path))

df["Referrals"].replace({0: 1}, inplace=True)
df["ReferralsReturned"].replace({0: 1}, inplace=True)

# FALL KPI - VISION ONLY

dfVisionTemp = df[df['ScreeningType'] == 'V']
dfVisionTemp.loc[:, 'Raw_Score'] = (dfVisionTemp['Screening']/dfVisionTemp['Enrollment'] * 100 * 0.99) + (dfVisionTemp['ReferralsReturned']/dfVisionTemp['Referrals'] * 100 * 0.01)
dfVision = round(dfVisionTemp.groupby('Campus_RowID')['Raw_Score'].mean(), 2)
dfVision = dfVision.reset_index()

dfVision['Raw_Score_Details'] = 'CustomDev.KPI_60800020001'
dfVision['Artifact_URL'] = 'SKYWARD'

# SPRING KPI - HEARING, ACANTHOSIS AND SPINAL

dfHearingTemp = df[df['ScreeningType'] == 'H']
dfHearingTemp.loc[:, 'Raw_Score'] = (dfHearingTemp['Screening']/dfHearingTemp['Enrollment'] * 100 * 0.99) + (dfHearingTemp['ReferralsReturned']/dfHearingTemp['Referrals'] * 100 * 0.01)
dfHearing = round(dfHearingTemp.groupby('Campus_RowID')['Raw_Score'].mean(), 2)
dfHearing = dfHearing.reset_index()

dfAcanthosisTemp = df[df['ScreeningType'] == 'A']
dfAcanthosisTemp.loc[:, 'Raw_Score'] = dfAcanthosisTemp['Screening']/dfAcanthosisTemp['Enrollment'] * 100
dfAcanthosis = round(dfAcanthosisTemp.groupby('Campus_RowID')['Raw_Score'].mean(), 2)
dfAcanthosis = dfAcanthosis.reset_index()

dfSpinalTemp = df[df['ScreeningType'] == 'S']
dfSpinalTemp.loc[:, 'Raw_Score'] = (dfSpinalTemp['Screening']/dfSpinalTemp['Enrollment'] * 100 * 0.99) + (dfSpinalTemp['ReferralsReturned']/dfSpinalTemp['Referrals'] * 100 * 0.01)
dfSpinal = round(dfSpinalTemp.groupby('Campus_RowID')['Raw_Score'].mean(), 2)
dfSpinal = dfSpinal.reset_index()

# DATA FRAME MERGE
frames = [dfHearing, dfAcanthosis, dfSpinal]
result = pd.concat(frames)
result = round(result.groupby('Campus_RowID')['Raw_Score'].mean(), 2)
result = result.reset_index()
result['Raw_Score_Details'] = 'CustomDev.KPI_60800020001'
result['Artifact_URL'] = 'SKYWARD'

# DATABASE INSERTION

Term = 1 if datetime.today().month in [11, 12, 1, 2] else (2 if datetime.today().month in [5, 6, 7] else 0)

# dfCampuses = dfCampuses.merge(dfVision, how='left', left_on='EntityID', right_on='Campus_RowID')
# dfVision = dfCampuses[['EntityID', 'Raw_Score', 'Raw_Score_Details', 'Artifact_URL']]
# dfVision.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
# dfCampuses = pd.read_csv(r'{}/Campuses.csv'.format(Bases.BaseKPI.source_files_path))
# dfCampuses = dfCampuses[dfCampuses['EntityCode']!=0]

# if Entities.KpiOperations.getSemesterNo().semesterNo.item() == 1:
if  Term == 1:
    Bases.BaseKPI.setKPIDetails(dfVision, True, 60800020001, True)
    print('Fall KPI record has been inserted to Fact_KPI_Campus table.')
else:
    Bases.BaseKPI.setKPIDetails(result, True, 60800020001, True)
    print('Spring KPI record has been inserted to Fact_KPI_Campus table.')



