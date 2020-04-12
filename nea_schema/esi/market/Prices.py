from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    DOUBLE as Double

from ... import Base

class Prices(Base):
    __tablename__ = 'mkt_Prices'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), primary_key=True, autoincrement=False)
    adjusted_price = Column(Double(unsigned=True))
    average_price = Column(Double(unsigned=True))

    @classmethod
    def esi_parse(cls, esi_return):
        data_items = esi_return.json()
        class_obj = [
            cls(**{
                **data,
                'record_time': dt.strptime(esi_return.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z'),
            }) for data in data_items
        ]
        return class_obj