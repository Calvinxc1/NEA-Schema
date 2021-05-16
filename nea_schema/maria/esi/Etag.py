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
    path = Column(VarChar(256), primary_key=True, autoincrement=False)
    last_modified = Column(DateTime)
    etag = Column(TinyText)
    
    @classmethod
    def esi_parse(cls, esi_return, orm=True):
        record_item = {
            'path': esi_return.url.split('?')[0],
            'last_modified': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag'),
        }
        if orm: record_item = cls(**record_item)
        return record_item
