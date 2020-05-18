"""
Operations Department's Manuel Entries
KPI: % of Timely submission of critical reports
This is a district-level KPI
Param1: Reports Submitted
It is a Yes/No scoring.
If all reports submitted on time  Param1= Yes and the KPI score will be 4,
if not Param1=No and the score will be 1.
"""

from BaseServices import Bases

df = Bases.BaseKPI.getManuelKPIData('OperationsKPI_FoodServices', 2)
df.rename(columns={df.columns[2]: 'Param1'}, inplace=True)
df["Raw_Score"] = df['Param1'].map(lambda x: 4 if x == 'Yes' else 1)
df['Raw_Score_Details'] = "State System"
df['Artifact_URL'] = 'https://drive.google.com/file/d/1Zzi3WCOTCeiiivJQn5UCiPszNKWRD1pQ/view?ts=5e723e32'
Bases.BaseKPI.setDistrictKPIDetails(df, True, 60600020001)



