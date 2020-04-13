from datetime import datetime as dt
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYTEXT as TinyText, \
    BOOLEAN as Boolean

from ... import Base

class Status(Base):
    __tablename__ = 'srv_ServerStatus'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    etag = Column(TinyText)
    players = Column(Integer(unsigned=True))
    server_version = Column(TinyText)
    start_time = Column(DateTime)
    vip = Column(Boolean, default=False)

    @classmethod
    def esi_parse(cls, esi_return):
        data = esi_return.json()
        class_obj = [cls(**{
            **data,
            'start_time': dt.strptime(data['start_time'], '%Y-%m-%dT%H:%M:%SZ'),
            'record_time': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag')[1:-1],
        })]
        return class_obj