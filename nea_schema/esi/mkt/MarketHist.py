from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    DATE as Date, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ... import Base

class MarketHist(Base):
    """ Schema for the mkt_History table
    
    Columns
    -------
    record_time: DateTime, Primary Key
        The cache time on the ESI return.
    etag: TinyText
        The ETag on the ESI return.
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
    type: Order.type_id <> Type.type_id
    region: Order.region_id <> Region.region_id
    """
    
    __tablename__ = 'mkt_History'
    
    ## Columns
    record_date = Column(Date, primary_key=True, autoincrement=False)
    etag = Column(TinyText)
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

    @classmethod
    def esi_parse(cls, esi_return):
        """ Parses and returns an ESI record
        
        Parses through a Requests return, returning a copy of the initialized class.
        
        Parameters
        ----------
        esi_return: Requests return
            A Requests return from an ESI endpoint.
            
        Returns
        -------
        class_obj: class
            An initialized copy of the class.
        """
        
        data_items = esi_return.json()
        class_obj = [
            cls(**{
                **data,
                'record_date': dt.strptime(data.pop('date'), '%Y-%m-%d'),
                'etag': esi_return.headers.get('Etag'),
                'region_id': int(esi_return.url.split('/')[5]),
                'type_id': int([
                    param.split('=')[1] for param
                    in esi_return.url.split('?')[1].split('&')
                    if param.startswith('type_id=')
                ][0]),
            }) for data in data_items
        ]
        return class_obj