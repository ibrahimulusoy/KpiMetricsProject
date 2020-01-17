import pyodbc

class BaseKPI:
    '''
    # You can use this connection like the below example; #

    import pandas as pd
    sql = 'SELECT * FROM HPS_METRICS.dbo.Dim_KPI'
    data = pd.read_sql(sql,conn)
    print(data.head)

    '''
    def dbConnection:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=localhost;'
                              'Database=HPS_METRICS;'
                              'Trusted_Connection=yes;')
        return conn

