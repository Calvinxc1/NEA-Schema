from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    BOOLEAN as Boolean, \
    DATETIME as DateTime, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class Order(Base):
    __tablename__ = 'mkt_Order'
    
    ## Columns
    record_time = Column(DateTime)
    order_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    system_id = Column(Integer(unsigned=True), ForeignKey('map_System.system_id'))
    region_id = Column(Integer(unsigned=True), ForeignKey('map_Region.region_id'))
    location_id = Column(BigInt(unsigned=True))
    is_buy_order = Column(Boolean)
    price = Column(Double(unsigned=True))
    duration = Column(Integer(unsigned=True))
    issued = Column(DateTime)
    range = Column(TinyText)
    volume_remain = Column(Integer(unsigned=True))
    volume_total = Column(Integer(unsigned=True))
    min_volume = Column(Integer(unsigned=True))
    
    ## Relationships
    type = relationship('Type')
    system = relationship('System')
    region = relationship('Region')
    corp_order = relationship(
        'CorpOrder',
        primaryjoin='Order.order_id == foreign(CorpOrder.order_id)',
        viewonly=True, uselist=False,
    )

    @classmethod
    def esi_parse(cls, esi_return, location_lookup, orm=True):
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        record_items = [{
            'record_time': record_time,
            **location_lookup.get(row['location_id'], {}),
            **row,
            'issued': dt.strptime(row['issued'], '%Y-%m-%dT%H:%M:%SZ'),
        } for row in esi_return.json()]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
