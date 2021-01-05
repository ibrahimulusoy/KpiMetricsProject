"""
KPI: % of required drills completed timely
Level: Campus-level KPI
Department: Programs - Student Safety and Discipline
Responsible Person: Jennifer Sabin
KPI ID: 60400040001

Notes:
Automated via Google API.
URL: https://docs.google.com/spreadsheets/d/1-UHdBwoigEn5AGhzSDznNmJEgBKgVUUa5YSZBW1o6Co/edit?ts=5fa5736e#gid=0
"""

import pandas as pd
import numpy as np
from BaseServices import Bases
from datetime import datetime


month = datetime.today().month
dfCampuses = pd.read_csv(r'{}\Campuses.csv'.format(Bases.BaseKPI.source_files_path))
schoolYear = str(dfCampuses['NumericYear'][0] - 1)[2:] + '-' + str(dfCampuses['NumericYear'][0])[2:]
Term = 1 if datetime.today().month in [11, 12, 1, 2] else (2 if datetime.today().month in [5, 6, 7] else 0)

dfTerm1 = dfYearlyDrills1 = Bases.BaseKPI.getManuelKPIData('{} Monthly Safety Report Compliance'.format(schoolYear), 0)
dfTerm2 = dfYearlyDrills2 = Bases.BaseKPI.getManuelKPIData('{} Monthly Safety Report Compliance'.format(schoolYear), 1)

# Sheet 0: 1st Semester
# dfTerm1 = Bases.BaseKPI.getManuelKPIData('{} Monthly Safety Report Compliance'.format(schoolYear), 0)
dfTerm1['EntityID'] = pd.to_numeric(dfTerm1['EntityID'])
dfTerm1 = dfTerm1.merge(dfCampuses, on='EntityID')
# dfFinal[''] = dfTerm1.iloc[:,4]
dfTerm1 = dfTerm1.iloc[:, [0, 6, 7, 8, 9, 10, 11]]
# required drills = all columns except n/a
dfTerm1['RequiredDrillCount'] = np.where(dfTerm1 != 'n/a', 1, 0).sum(axis=1) - 1
# completed drills = required minus null columns
dfTerm1['CompletedDrillCount'] = dfTerm1['RequiredDrillCount'] - np.where(dfTerm1 == "", 1, 0).sum(axis=1)
dfTerm1 = dfTerm1[['EntityID', 'RequiredDrillCount', 'CompletedDrillCount']]
dfTerm1 = dfTerm1.groupby(['EntityID']).agg({'RequiredDrillCount': 'sum', 'CompletedDrillCount': 'sum'}).reset_index()

# Sheet 1: 2nd Semester
# dfTerm2 = Bases.BaseKPI.getManuelKPIData('{} Monthly Safety Report Compliance'.format(schoolYear), 1)
dfTerm2['EntityID'] = pd.to_numeric(dfTerm2['EntityID'])
dfTerm2 = dfTerm2.merge(dfCampuses, on='EntityID')
dfTerm2 = dfTerm2.iloc[:, [0, 6, 7, 8, 9, 10, 11, 12]]
dfTerm2['RequiredDrillCount'] = np.where(dfTerm2 != 'n/a', 1, 0).sum(axis=1) - 1
dfTerm2['CompletedDrillCount'] = dfTerm2['RequiredDrillCount'] - np.where(dfTerm2 == "", 1, 0).sum(axis=1)
dfTerm2 = dfTerm2[['EntityID', 'RequiredDrillCount', 'CompletedDrillCount']]
dfTerm2 = dfTerm2.groupby(['EntityID']).agg({'RequiredDrillCount': 'sum', 'CompletedDrillCount': 'sum'}).reset_index()

dfFinal = pd.DataFrame()
dfFinal['EntityID'] = dfTerm1['EntityID']
dfFinal['RequiredDrillCount'] = dfTerm1['RequiredDrillCount'] + dfTerm2['RequiredDrillCount']
dfFinal['CompletedDrillCount'] = dfTerm1['CompletedDrillCount'] + dfTerm2['CompletedDrillCount']
# dfFinal = dfFinal[dfFinal['EntityID'] != ''].drop_duplicates().reset_index(drop=True)

if Term == 1:
    dfTerm1['Raw_Score'] = (dfTerm1['CompletedDrillCount'] / dfTerm1['RequiredDrillCount']) * 100
    dfTerm1['Raw_Score_Details'] = "Monthly Safety Report Compliance"
    dfTerm1['Artifact_URL'] = 'https://docs.google.com/spreadsheets/d/1-UHdBwoigEn5AGhzSDznNmJEgBKgVUUa5YSZBW1o6Co/edit#gid=0'
    dfTerm1.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
    Bases.BaseKPI.setKPIDetails(dfTerm1, True, 81200010001, True)
elif Term == 2:
    dfTerm2['Raw_Score'] = (dfTerm2['CompletedDrillCount'] / dfTerm2['RequiredDrillCount']) * 100
    dfTerm2['Raw_Score_Details'] = "Monthly Safety Report Compliance"
    dfTerm2['Artifact_URL'] = 'https://docs.google.com/spreadsheets/d/1-UHdBwoigEn5AGhzSDznNmJEgBKgVUUa5YSZBW1o6Co/edit#gid=0'
    dfTerm2.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
    Bases.BaseKPI.setKPIDetails(dfTerm2, True, 81200010001, True)
else:
    dfYearlyDrills1 = dfYearlyDrills1.iloc[:, [0, 4, 5]][dfYearlyDrills1['EntityID'] != ''].reset_index(drop=True)
    dfYearlyDrills2 = dfYearlyDrills2.iloc[:, [0, 4, 5]][dfYearlyDrills2['EntityID'] != ''].reset_index(drop=True)
    dfYearlyDrills1['RequiredDrillCount'] = np.where(dfYearlyDrills1 != 'n/a', 1, 0).sum(axis=1) - 1
    dfYearlyDrills2['RequiredDrillCount'] = np.where(dfYearlyDrills2 != 'n/a', 1, 0).sum(axis=1) - 1
    dfYearlyDrills1['CompletedDrillCount'] = dfYearlyDrills1['RequiredDrillCount'] - np.where(dfYearlyDrills1 == "", 1,
                                                                                              0).sum(axis=1)
    dfYearlyDrills2['CompletedDrillCount'] = dfYearlyDrills2['RequiredDrillCount'] - np.where(dfYearlyDrills2 == "", 1,
                                                                                              0).sum(axis=1)
    dfYearlyDrills1 = dfYearlyDrills1.groupby(['EntityID']).agg(
        {'RequiredDrillCount': 'sum', 'CompletedDrillCount': 'sum'}).reset_index()
    dfYearlyDrills2 = dfYearlyDrills2.groupby(['EntityID']).agg(
        {'RequiredDrillCount': 'sum', 'CompletedDrillCount': 'sum'}).reset_index()
    dfYearlyDrills1['YearlyDrills'] = np.where(
        dfYearlyDrills1['CompletedDrillCount'] > dfYearlyDrills2['CompletedDrillCount'],
        dfYearlyDrills1['CompletedDrillCount'], dfYearlyDrills2['CompletedDrillCount'])
    dfFinal['RequiredDrillCount'] = dfFinal['RequiredDrillCount'] + 2
    dfFinal['CompletedDrillCount'] = dfFinal['CompletedDrillCount'] + dfYearlyDrills1['YearlyDrills']
    # Calculate final raw scores
    dfFinal['Raw_Score'] = (dfFinal['CompletedDrillCount'] / dfFinal['RequiredDrillCount']) * 100
    dfFinal['Raw_Score_Details'] = "Monthly Safety Report Compliance"
    dfFinal['Artifact_URL'] = 'https://docs.google.com/spreadsheets/d/1-UHdBwoigEn5AGhzSDznNmJEgBKgVUUa5YSZBW1o6Co/edit#gid=0'
    dfFinal.rename(columns={'EntityID': 'Campus_RowID'}, inplace=True)
    Bases.BaseKPI.setKPIDetails(dfFinal, True, 81200010001, True)



