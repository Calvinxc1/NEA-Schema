from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class Jumps(Base):
    __tablename__ = 'uni_Jumps'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    etag = Column(TinyText)
    system_id = Column(Integer(unsigned=True), ForeignKey('map_System.system_id'), primary_key=True, autoincrement=False)
    ship_jumps = Column(Integer(unsigned=True))
    
    ## Relationships
    system = relationship('System')

    @classmethod
    def esi_parse(cls, esi_return, orm=True):
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        etag = esi_return.headers.get('Etag')
        record_items = [{
            'record_time': record_time,
            'etag': etag,
            **row,
        } for row in esi_return.json()]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
