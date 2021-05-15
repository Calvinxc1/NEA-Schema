from datetime import datetime as dt, timedelta as td
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    DATE as Date, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class MarketHistory(Base):
    __tablename__ = 'mkt_History'
    
    ## Columns
    region_id = Column(Integer(unsigned=True), ForeignKey('map_Region.region_id'), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), primary_key=True, autoincrement=False)
    record_date = Column(Date, primary_key=True, autoincrement=False, index=True)
    order_count = Column(BigInt(unsigned=True))
    volume = Column(BigInt(unsigned=True))
    lowest = Column(Double(unsigned=True))
    average = Column(Double(unsigned=True))
    highest = Column(Double(unsigned=True))
    
    ## Relationships
    type = relationship('Type')
    region = relationship('Region')

    @classmethod
    def esi_parse(cls, esi_return, orm=True, days_back=7):
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        region_id = int(esi_return.url.split('/')[5])
        type_id = int([
            param.split('=')[1] for param
            in esi_return.url.split('?')[1].split('&')
            if param.startswith('type_id=')
        ][0])
        
        earliest_date = record_time.date() - td(days=days_back-1)\
            if days_back else date(1970,1,1)
            
        record_items = [{
            'record_time': record_time,
            **row,
            'region_id': region_id,
            'type_id': type_id,
        } for row in esi_return.json()
            if dt.strptime(row['date'], '%Y-%m-%d') >= earliest_date
        ]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
