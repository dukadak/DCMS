from sqlalchemy import Column, String
from dcms.conn_db import Base

class DcmsAssets:
    __tablename__ = 'dcms_assets'
    asset_tag = Column(String(20))
    aseet_model = Column(String(10))
    asset_serial_number = Column(String(30))
    hostname = Column(String(50))