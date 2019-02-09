from flask import Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import dbConn_info

mod = Blueprint('conn_db', __name__)

dbConn = 'mysql+pymysql://'+dbConn_info.dbUser+':'+dbConn_info.dbPasswd+'@'+dbConn_info.dbHost+':'+dbConn_info.dbPort+'/dcmsdb?charset=utf8'

engine = create_engine(dbConn, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import dcms.db_models
    Base.metadata.create_all(bind=engine)
    db_session.close()
    