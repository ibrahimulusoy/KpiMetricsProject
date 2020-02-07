'''
KPI: Number of Enrollment
'''

import pandas as pd
from EntityServices import Entities


df1 = pd.read_csv(r'C:\Users\eatakahraman\Desktop\KPI_60100010001.csv')
df2 = pd.read_csv(r'C:\Users\eatakahraman\Desktop\KPI_60100010001_Budgeted.csv')

df = pd.merge(df1, df2, on='EntityShortName')
#df = df.reset_index(drop=True)


df["Division"] = df["CurrentEnrollment"] / df["BudgetedEnrollment"] * 100
df["KpiScore"] = df["Division"].apply(lambda x: 4 if x >= 102 else (3 if x >= 100 else (2 if x >= 98 else (1 if x >= 97 else 0))))

kpiDetails = Entities.KpiOperations.getKPIDetails(60100010001)
df.rename(columns = {'EntityID':'Campus_RowID'}, inplace = True)
df['Term_RowID'] = int(kpiDetails['Term_RowID'])
df['KPI_RowID']= int(kpiDetails['KPI_Row_Id'])
df['Category_RowID']= int(kpiDetails['CategoryKey'])
df['Department_RowID']=int(kpiDetails['DepartmentKey'])
df['Is_KPI_Applicable']=int(kpiDetails['Is_KPI_Applicable'])
adjustedWeight = int(kpiDetails['Is_KPI_Applicable']) * int(kpiDetails['Weight'])
df['Adjusted_Weight']= adjustedWeight
df['Adjusted_Score'] = df['Adjusted_Weight'] * df['KpiScore']

districts = Entities.KpiOperations.getDistrictsForAllCampuses()
df = pd.merge(df, districts, left_on='Campus_RowID', right_on='CampusKey')
#Entities.insertFactKPICampuses(df,"Fact_KPI_Campus")
#
del(df['CampusKey'])
#df.to_csv(r'C:\Users\eatakahraman\Desktop\KPI.csv')
Entities.KpiOperations.insertFactKPICampuses(df,'Fact_KPI_Campus')