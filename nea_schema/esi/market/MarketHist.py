from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import \
    DATE as Date, \
    INTEGER as Integer, \
    BIGINT as BigInt, \
    DOUBLE as Double

from ... import Base

class MarketHist(Base):
    __tablename__ = 'mkt_History'
    
    ## Columns
    record_date = Column(Date, primary_key=True, autoincrement=False)
    region_id = Column(Integer(unsigned=True), ForeignKey('map_Region.region_id'), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), primary_key=True, autoincrement=False)
    order_count = Column(BigInt(unsigned=True))
    volume = Column(BigInt(unsigned=True))
    lowest = Column(Double(unsigned=True))
    average = Column(Double(unsigned=True))
    highest = Column(Double(unsigned=True))

    @classmethod
    def esi_parse(cls, esi_return):
        data_items = esi_return.json()
        class_obj = [
            cls(**{
                **data,
                'record_date': dt.strptime(data.pop('date'), '%Y-%m-%d'),
            }) for data in data_items
        ]
        return class_obj