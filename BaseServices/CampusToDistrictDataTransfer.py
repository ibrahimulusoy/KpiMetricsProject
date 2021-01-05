import datetime
from EntityServices import Entities


df=Entities.KpiOperations.getManualKPIsCampusData(14)
print(df)
df['Raw_Score']=''
df['Raw_Score_Details']=''
df['Artifact_URL']=''
df['DmlUserId']=''
#df['DmlDateTime']=datetime.datetime.now()

Entities.KpiOperations.insertFactKPI(df, 'Fact_KPI')