from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYINT as TinyInt, \
    TINYTEXT as TinyText

from ...Base import Base

class CorpBlueprint(Base):    
    __tablename__ = 'corp_Blueprint'
    
    ## Columns
    record_time = Column(DateTime)
    etag = Column(TinyText)
    item_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    location_flag = Column(TinyText)
    location_id = Column(BigInt, ForeignKey('corp_Asset.item_id'))
    material_efficiency = Column(TinyInt(unsigned=True))
    quantity = Column(Integer)
    runs = Column(Integer)
    time_efficiency = Column(TinyInt(unsigned=True))
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), ForeignKey('bp_Blueprint.type_id'))
    
    ## Relationships
    type = relationship('Type')
    blueprint = relationship('Blueprint', viewonly=True)
    #asset = relationship('CorpAsset')
    location = relationship('CorpAsset')
    industry = relationship('CorpIndustry', primaryjoin='CorpBlueprint.item_id == foreign(CorpIndustry.blueprint_id)', back_populates='blueprint', viewonly=True, uselist=True)

    @classmethod
    def esi_parse(cls, esi_return):
        class_obj = [cls(**{
            **data,
            'record_time': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag'),
        }) for data in esi_return.json()]
        return class_obj
