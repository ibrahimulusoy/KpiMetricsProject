from sqlalchemy import create_engine
import kpiconfig as cfg
import pandas as pd

class BaseKPI():
    global engine

    engine = create_engine('mssql+pyodbc://{}:{}@{}/{}?driver={}'.format(cfg.mssql['Username'], cfg.mssql['Password'], cfg.mssql['Server'], cfg.mssql['Database'], cfg.mssql['Driver']))
    def dbConnection():
        return engine





