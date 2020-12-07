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
if Term == 1:
    # Sheet 0: 1st Semester
    df = Bases.BaseKPI.getManuelKPIData('{} Monthly Safety Report Compliance'.format(schoolYear), 0)
    df['EntityID'] = pd.to_numeric(df['EntityID'])
    df = df.merge(dfCampuses, on='EntityID')
    df = df.iloc[:, [0, 6, 7, 8, 9, 10, 11]]
    # required drills = all columns except n/a
    df['RequiredDrillCount'] = np.where(df != 'n/a', 1, 0).sum(axis=1) - 1
    # completed drills = required minus null columns
    df['CompletedDrillCount'] = df['RequiredDrillCount'] - np.where(df == "", 1, 0).sum(axis=1)
    df['Raw_Score'] = (df['CompletedDrillCount'] / df['RequiredDrillCount']) * 100
elif Term == 2:
    # Sheet 1: 2nd Semester
    df = Bases.BaseKPI.getManuelKPIData('{} Monthly Safety Report Compliance'.format(schoolYear), 1)
    df['EntityID'] = pd.to_numeric(df['EntityID'])
    df = df.merge(dfCampuses, on='EntityID')
    df = df.iloc[:, [0, 6, 7, 8, 9, 10, 11, 12]]
    df['RequiredDrillCount'] = np.where(df != 'n/a', 1, 0).sum(axis=1) - 1
    df['CompletedDrillCount'] = df['RequiredDrillCount'] - np.where(df == "", 1, 0).sum(axis=1)
    df['Raw_Score'] = (df['CompletedDrillCount'] / df['RequiredDrillCount']) * 100
else:
    dfFirstSemester = Bases.BaseKPI.getManuelKPIData('{} Monthly Safety Report Compliance'.format(schoolYear), 0)
    dfSecondSemester = Bases.BaseKPI.getManuelKPIData('{} Monthly Safety Report Compliance'.format(schoolYear), 1)

print()
