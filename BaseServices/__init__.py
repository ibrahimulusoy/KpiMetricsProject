import pyodbc
import kpiconfig as cfg

class BaseKPI():
    def dbConnection():

        x = 'Driver = %s;Server = %s;Database = %s;Trusted_Connection=%s;' % (cfg.mssql['Driver'],cfg.mssql['Server'],cfg.mssql['Database'],'yes')
        #conn = pyodbc.connect('Driver = {%s};Server = %s;Database = %s;Trusted_Connection=%s;' % (cfg.mssql['Driver'],cfg.mssql['Server'],cfg.mssql['Database'],'yes'))

        conn = pyodbc.connect('Driver = {SQL Server};'
                              'Server = localhost;'
                              'Database = HPS_METRICS;'
                              'Trusted_Connection=yes;')




        return conn



#connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'])
#print("Hello {}, your balance is {}.".format("Adam", 230.2346))
#self.db = pyodbc.connect('driver={%s};server=%s;database=%s;uid=%s;pwd=%s' % ( driver, server, db, user, password ) )
#self.db = pyodbc.connect(driver=driver, server=server, database=db,trusted_connection='yes')