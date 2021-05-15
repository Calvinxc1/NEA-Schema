from datetime import datetime as dt
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    TINYTEXT as TinyText, \
    VARCHAR as VarChar

from ..Base import Base

class Etag(Base):
    __tablename__ = 'esi_Etag'
    
    ## Columns
    path = Column(VarChar(60), primary_key=True, autoincrement=False)
    last_modified = Column(DateTime)
    etag = Column(TinyText)
    
    @classmethod
    def esi_parse(cls, esi_return, orm=True):
        record_items = [{
            'path': esi_return.url.split('?')[0],
            'last_modified': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag'),
        }]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
