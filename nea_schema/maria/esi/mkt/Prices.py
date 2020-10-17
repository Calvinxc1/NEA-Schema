from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class Prices(Base):
    """ Schema for the mkt_Prices table
    
    Columns
    -------
    record_time: DateTime, Primary Key
        The cache time on the ESI return.
    etag: TinyText
        The ETag on the ESI return.
    type_id: Unsigned Integer, Primary Key
        The type that the data is for.
    adjusted_price: Unsigned Double
        The adjusted price, given record_time and type_id.
    average_price: Unsigned Double
        The average price, given record_time and type_id.
        
    Relationships
    -------------
    type: Prices.type_id <> Type.type_id
    """
    
    __tablename__ = 'mkt_Prices'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    etag = Column(TinyText)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'), primary_key=True, autoincrement=False)
    adjusted_price = Column(Double(unsigned=True))
    average_price = Column(Double(unsigned=True))
    
    ## Relationships
    type = relationship('Type')

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
                'record_time': dt.strptime(esi_return.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z'),
                'etag': esi_return.headers.get('Etag'),
            }) for data in data_items
        ]
        return class_obj