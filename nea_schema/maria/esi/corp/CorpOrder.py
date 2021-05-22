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

class CorpOrder(Base):    
    __tablename__ = 'corp_Order'
    
    ## Columns
    record_time = Column(DateTime)
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
    region_id = Column(BigInt(unsigned=True), ForeignKey('map_Region.region_id'))
    state = Column(TinyText)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    volume_remain = Column(Integer(unsigned=True))
    volume_total = Column(Integer(unsigned=True))
    wallet_division = Column(Integer(unsigned=True))
    
    ## Relationships
    type = relationship('Type')
    region = relationship('Region')
    order = relationship(
        'Order',
        primaryjoin='CorpOrder.order_id == foreign(Order.order_id)',
        viewonly=True, uselist=False,
    )
    compete = relationship(
        'Order',
        primaryjoin="""and_(
            CorpOrder.type_id == foreign(Order.type_id),
            CorpOrder.region_id == foreign(Order.region_id),
            CorpOrder.is_buy_order == foreign(Order.is_buy_order),
            CorpOrder.order_id != foreign(Order.order_id),
        )""", viewonly=True, uselist=True,
    )

    @classmethod
    def esi_parse(cls, esi_return, orm=True):
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        record_items = [{
            'record_time': record_time,
            **row,
            'escrow': row.get('escrow', 0),
            'is_buy_order': row.get('is_buy_order', False),
            'issued': dt.strptime(row.get('issued'), '%Y-%m-%dT%H:%M:%SZ'),
            'min_volume': row.get('min_volume', 0),
            'state': row.get('state', 'active'),
        } for row in esi_return.json()]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
