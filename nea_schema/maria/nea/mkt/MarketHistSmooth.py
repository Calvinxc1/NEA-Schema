from datetime import datetime as dt, timedelta as td
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    CHAR as Char, \
    DATE as Date, \
    DOUBLE as Double, \
    INTEGER as Integer
    

from ... import Base

class MarketHistSmooth(Base):
    """ Schema for the mkt_History table
    
    Columns
    -------
    record_time: DateTime, Primary Key
        The cache time on the ESI return.
    model_id: Char(24)
        The _id value of the model being used (located in MongoDB.NewEdenAnalytics.Model)
    region_id: Unsigned Integer, Primary Key
        The region the history data is for.
    type_id: Unsigned Integer, Primary Key
        The type the history data is for.
    order_count: Unsigned Big Integer
        How many orders were transacted against (confirm), given record_time, region_id, and type_id.
    volume: Unsigned Big Integer
        How many units were transacted, given record_time, region_id, and type_id.
    lowest: Unsigned Double
        What was the lowest unit price transacted, given record_time, region_id, and type_id.
    average: Unsigned Double
        What was the mean unit price transacted, given record_time, region_id, and type_id.
    highest: Unsigned Double
        What was the highest unit price transacted, given record_time, region_id, and type_id.
        
    Relationships
    -------------
    type: MarketHistSmooth.type_id <> Type.type_id
    region: MarketHistSmooth.region_id <> Region.region_id
    """
    
    __tablename__ = 'mkt_HistorySmooth'
    
    ## Columns
    record_date = Column(Date, primary_key=True, autoincrement=False)
    model_id = Column(Char(24), primary_key=True, autoincrement=False)
    region_id = Column(Integer(unsigned=True), ForeignKey('map_Region.region_id'), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), primary_key=True, autoincrement=False)
    order_count = Column(BigInt(unsigned=True))
    volume = Column(BigInt(unsigned=True))
    lowest = Column(Double(unsigned=True))
    average = Column(Double(unsigned=True))
    highest = Column(Double(unsigned=True))
    
    ## Relationships
    type = relationship('Type')
    region = relationship('Region')