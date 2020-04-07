"""
KPI 7: % of Screenings complete (vision, hearing, spinal, and diabetes)
"""

import pandas as pd
from BaseServices import Bases

df = pd.read_csv(r'C:\Users\bballiyev\OneDrive - Harmony Public Schools\Desktop\KPI Project\KPI_60800020001.csv')

df["Referrals"].replace({0: 1}, inplace=True)
df["ReferralsReturned"].replace({0: 1}, inplace=True)

# VISION SCOPE
dfVisionTemp = df[df['ScreeningType'] == 'V']
dfVisionTemp.loc[:, 'Raw_Score'] = (dfVisionTemp['Screening']/dfVisionTemp['Enrollment'] * 100 * 0.99) + (dfVisionTemp['ReferralsReturned']/dfVisionTemp['Referrals'] * 100 * 0.01)
dfVision = round(dfVisionTemp.groupby('Campus_RowID')['Raw_Score'].mean(), 2)

# HEARING SCOPE
dfHearingTemp = df[df['ScreeningType'] == 'H']
dfHearingTemp.loc[:, 'Raw_Score'] = (dfHearingTemp['Screening']/dfHearingTemp['Enrollment'] * 100 * 0.99) + (dfHearingTemp['ReferralsReturned']/dfHearingTemp['Referrals'] * 100 * 0.01)
dfHearing = round(dfHearingTemp.groupby('Campus_RowID')['Raw_Score'].mean(), 2)

# ACANTHOSIS SCOPE
dfAcanthosisTemp = df[df['ScreeningType'] == 'A']
dfAcanthosisTemp.loc[:, 'Raw_Score'] = dfAcanthosisTemp['Screening']/dfAcanthosisTemp['Enrollment'] * 100
dfAcanthosis = round(dfAcanthosisTemp.groupby('Campus_RowID')['Raw_Score'].mean(), 2)

# SPINAL SCOPE
dfSpinalTemp = df[df['ScreeningType'] == 'S']
dfSpinalTemp.loc[:, 'Raw_Score'] = (dfSpinalTemp['Screening']/dfSpinalTemp['Enrollment'] * 100 * 0.99) + (dfSpinalTemp['ReferralsReturned']/dfSpinalTemp['Referrals'] * 100 * 0.01)
dfSpinal = round(dfSpinalTemp.groupby('Campus_RowID')['Raw_Score'].mean(), 2)

# SPRING KPI
dfVision['Raw_Score_Details'] = 'CustomDev.KPI_60800020001'
dfVision['Artifact_URL'] = 'SKYWARD'

Bases.BaseKPI.setKPIDetails(dfVision, False, 60800020001)
print('This KPI records has been inserted to Fact_KPI_Campus table.')
# print(dfVision.to_string())

# df['Raw_Score_Details'] = 'CustomDev.KPI_60800020001'
# df['Artifact_URL'] = 'SKYWARD'

# Bases.BaseKPI.setKPIDetails(df, False, 60800020001)
# print('This KPI records has been inserted to Fact_KPI_Campus table.')
# print(dfVisionTemp.to_string())
# print(dfVision.to_string())
# print(dfHearing.to_string())
# print(dfAcanthosis.to_string())
# print(dfSpinal.to_string())