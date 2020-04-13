from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ... import Base

class Prices(Base):
    __tablename__ = 'mkt_Prices'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    etag = Column(TinyText)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), primary_key=True, autoincrement=False)
    adjusted_price = Column(Double(unsigned=True))
    average_price = Column(Double(unsigned=True))
    
    ## Relationships
    system = relationship('Type')

    @classmethod
    def esi_parse(cls, esi_return):
        data_items = esi_return.json()
        class_obj = [
            cls(**{
                **data,
                'record_time': dt.strptime(esi_return.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z'),
                'etag': esi_return.headers.get('Etag'),
            }) for data in data_items
        ]
        return class_obj