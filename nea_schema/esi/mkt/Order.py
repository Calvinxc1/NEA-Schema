from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import DATETIME as DateTime, \
    INTEGER as Integer, \
    BOOLEAN as Boolean, \
    BIGINT as BigInt, \
    DOUBLE as Double, \
    TINYTEXT as TinyText

from ... import Base

class Order(Base):
    __tablename__ = 'mkt_Order'
    
    ## Columns
    record_time = Column(DateTime)
    order_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    region_id = Column(Integer(unsigned=True), ForeignKey('map_Region.region_id'))
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    system_id = Column(Integer(unsigned=True), ForeignKey('map_System.system_id'))
    location_id = Column(BigInt(unsigned=True))
    is_buy_order = Column(Boolean)
    price = Column(Double(unsigned=True))
    duration = Column(Integer(unsigned=True))
    issued = Column(DateTime)
    range = Column(TinyText)
    volume_remain = Column(Integer(unsigned=True))
    volume_total = Column(Integer(unsigned=True))
    min_volume = Column(Integer(unsigned=True))

    @classmethod
    def esi_parse(cls, esi_return):
        data_items = esi_return.json()
        class_obj = [
            cls(**{
                **data,
                'issued': dt.strptime(data['issued'], '%Y-%m-%dT%H:%M:%SZ'),
                'record_time': dt.strptime(esi_return.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z'),
            }) for data in data_items
        ]
        return class_obj