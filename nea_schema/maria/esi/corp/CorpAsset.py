from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    BOOLEAN as Boolean, \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYINT as TinyInt, \
    TINYTEXT as TinyText

from ...Base import Base

class CorpAsset(Base):    
    __tablename__ = 'corp_Asset'
    
    ## Columns
    record_time = Column(DateTime)
    is_blueprint_copy = Column(Boolean)
    is_singleton = Column(Boolean)
    item_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    item_name = Column(TinyText)
    location_flag = Column(TinyText)
    location_id = Column(BigInt(unsigned=True))
    location_type = Column(TinyText)
    quantity = Column(Integer)
    station_id = Column(BigInt(unsigned=True))
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    
    ## Relationships
    type = relationship('Type')
    parent = relationship(
        'CorpAsset',
        primaryjoin='CorpAsset.location_id == foreign(CorpAsset.item_id)',
        viewonly=True, uselist=False,
    )
    child = relationship(
        'CorpAsset',
        primaryjoin='CorpAsset.item_id == foreign(CorpAsset.location_id)',
        viewonly=True, uselist=True,
    )
    blueprint = relationship(
        'CorpBlueprint',
        primaryjoin='CorpAsset.item_id == foreign(CorpBlueprint.item_id)',
        viewonly=True, uselist=False,
    )

    @classmethod
    def esi_parse(cls, esi_return, orm=True):
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        record_items = [{
            'record_time': record_time,
            **row,
        } for row in esi_return.json()]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
