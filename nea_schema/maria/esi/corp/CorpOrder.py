from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    BOOLEAN as Boolean, \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYINT as TinyInt, \
    TINYTEXT as TinyText, \
    DOUBLE as Double, \
    FLOAT as Float

from ...Base import Base

class CorpOrder(Base):    
    __tablename__ = 'corp_Order'
    
    ## Columns
    record_time = Column(DateTime)
    etag = Column(TinyText)
    duration = Column(Integer(unsigned=True))
    escrow = Column(Double(unsigned=True))
    is_buy_order = Column(Boolean)
    issued = Column(DateTime)
    issued_by = Column(BigInt(unsigned=True))
    location_id = Column(BigInt(unsigned=True))
    min_volume = Column(BigInt(unsigned=True))
    order_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    price = Column(Double(unsigned=True))
    range = Column(TinyText)
    region_id = Column(Integer(unsigned=True))
    state = Column(TinyText)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    volume_remain = Column(Integer(unsigned=True))
    volume_total = Column(Integer(unsigned=True))
    wallet_division = Column(Integer(unsigned=True))
    
    ## Relationships
    type = relationship('Type')
    order = relationship('Order', primaryjoin='CorpOrder.order_id == foreign(Order.order_id)', viewonly=True, uselist=False)

    @classmethod
    def esi_parse(cls, esi_return):
        class_obj = [cls(**{
            'record_time': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag'),
            'duration': row.get('duration'),
            'escrow': row.get('escrow', 0),
            'is_buy_order': row.get('is_buy_order', False),
            'issued': dt.strptime(row.get('issued'), '%Y-%m-%dT%H:%M:%SZ'),
            'issued_by': row.get('issued_by'),
            'location_id': row.get('location_id'),
            'min_volume': row.get('min_volume', 0),
            'order_id': row.get('order_id'),
            'price': row.get('price'),
            'range': row.get('range'),
            'region_id': row.get('region_id'),
            'state': row.get('state', 'active'),
            'type_id': row.get('type_id'),
            'volume_remain': row.get('volume_remain'),
            'volume_total': row.get('volume_total'),
            'wallet_division': row.get('wallet_division'),
        }) for row in esi_return.json()]
        return class_obj
