from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    CHAR as Char, \
    DATE as Date, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TINYINT as TinyInt
    
from ...Base import Base

class MarketState(Base):
    __tablename__ = 'mdl_MarketState'
    
    ## Columns
    region_id = Column(Integer(unsigned=True), ForeignKey('map_Region.region_id'), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), primary_key=True, autoincrement=False)
    record_date = Column(Date, primary_key=True, autoincrement=False, index=True)
    model_id = Column(Char(24), primary_key=True, autoincrement=False)
    dim_idx = Column(TinyInt(unsigned=True), primary_key=True, autoincrement=False)
    order_count_actual = Column(Double)
    volume_actual = Column(Double)
    lowest_actual = Column(Double)
    average_actual = Column(Double)
    highest_actual = Column(Double)
    order_count_smooth = Column(Double)
    volume_smooth = Column(Double)
    lowest_smooth = Column(Double)
    average_smooth = Column(Double)
    highest_smooth = Column(Double)
    
    ## Relationships
    type = relationship('Type')
    region = relationship('Region')