import pandas as pd
from BaseServices import BaseKPI

sql = 'SELECT * FROM HPS_METRICS_QA.dbo.Dim_KPI'
conn = BaseKPI.dbConnection()
data = pd.read_sql(sql, conn)
print(data.head)

