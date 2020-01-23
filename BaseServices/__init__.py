import pyodbc

class BaseKPI:

    def dbConnection():
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=localhost;'
                              'Database=HPS_METRICS;'
                              'Trusted_Connection=yes;')
        return conn


