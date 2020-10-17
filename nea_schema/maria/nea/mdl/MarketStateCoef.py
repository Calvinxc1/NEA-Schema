from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    CHAR as Char, \
    DATE as Date, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TINYINT as TinyInt
    
from ...Base import Base

class MarketStateCoef(Base):
    __tablename__ = 'mdl_MarketStateCoef'
    
    ## Columns
    region_id = Column(Integer(unsigned=True), ForeignKey('map_Region.region_id'), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), primary_key=True, autoincrement=False)
    model_id = Column(Char(24), primary_key=True, autoincrement=False)
    dim_idx = Column(TinyInt(unsigned=True), primary_key=True, autoincrement=False)
    order_count_coef = Column(Double)
    volume_coef = Column(Double)
    lowest_coef = Column(Double)
    average_coef = Column(Double)
    highest_coef = Column(Double)
    last_updated = Column(Date)
    
    ## Relationships
    type = relationship('Type')
    region = relationship('Region')