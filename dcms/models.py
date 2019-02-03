from dcms import db

class Assets(db.Model):
    __tablename__ = "assets"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    num = db.Column(db.Integer, unique=True, nullable=False, autoincrement=True)
    asset_name = db.Column(db.String(50))
    count = db.Column(db.Integer, nullable=False)
    serial_num = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)

    def __init__(self, name, count, serial_num):
        self.asset_name = name
        self.serial_num = serial_num
        self.count = count