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
    """ Schema for the mkt_Orders table
    
    Columns
    -------
    record_time: DateTime
        The cache time on the ESI return.
    etag: TinyText
        The ETag on the ESI return.
    order_id: Unsigned Big Integer, Primary Key
        Unique ID of the order.
    type_id: Unsigned Integer
        Type of item in the order.
    system_id: Unsigned Integer
        System the order is located in.
    location_id: Unsigned Big Integer
        Location (station) the order is located in.
    is_buy_order: Boolean
        Is the order a buy order (True) or a sell order (False)?
    price: Unsigned Double
        What is the per-unit price of the order.
    duration: Unsigned Integer
        How many days will the order last, since issued.
    issued: DateTime
        When was the order issued?
    range: Tiny Text
        What range was the order set for? Numeric is in jumps from system_id.
        Enumerates: [station, region, solarsystem, 1, 2, 3, 4, 5, 10, 20, 30, 40]
    volume_remain: Unsigned Integer
        How many items remain in the order?
    volume_total: Unsigned Integer
        How many items were in the order when it was issued?
    min_volume: Unsigned Integer
        What is the minimum number of items to be purchased to transact against the order?
        
    Relationships
    -------------
    type: Order.type_id <> Type.type_id
    system: Order.system_id <> System.system_id
    """
    
    __tablename__ = 'mkt_Order'
    
    ## Columns
    record_time = Column(DateTime)
    etag = Column(TinyText)
    order_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    system_id = Column(Integer(unsigned=True), ForeignKey('map_System.system_id'))
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
                'issued': dt.strptime(data['issued'], '%Y-%m-%dT%H:%M:%SZ'),
                'record_time': dt.strptime(esi_return.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z'),
                'etag': esi_return.headers.get('Etag'),
            }) for data in data_items
        ]
        return class_obj