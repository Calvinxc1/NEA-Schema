from datetime import datetime as dt
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class Status(Base):
    __tablename__ = 'srv_ServerStatus'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    players = Column(Integer(unsigned=True))
    server_version = Column(TinyText)
    start_time = Column(DateTime)
    vip = Column(Boolean, default=False)

    @classmethod
    def esi_parse(cls, esi_return, orm=True):
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        row = esi_return.json()
        record_items = [{
            'record_time': record_time,
            **row,
            'start_time': dt.strptime(row['start_time'], '%Y-%m-%dT%H:%M:%SZ'),
        }]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
