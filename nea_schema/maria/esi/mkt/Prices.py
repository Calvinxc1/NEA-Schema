from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class Prices(Base):
    __tablename__ = 'mkt_Prices'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), primary_key=True, autoincrement=False)
    adjusted_price = Column(Double(unsigned=True))
    average_price = Column(Double(unsigned=True))
    
    ## Relationships
    type = relationship('Type')

    @classmethod
    def esi_parse(cls, esi_return, orm=True):
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        record_items = [{
            'record_time': record_time,
            **row,
        } for row in esi_return.json()]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items