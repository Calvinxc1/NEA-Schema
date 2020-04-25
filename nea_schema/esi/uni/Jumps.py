from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ... import Base

class Jumps(Base):
    """ Schema for the uni_Jumps table
    
    Columns
    -------
    record_time: DateTime, Primary Key
        The cache time on the ESI return.
    etag: TinyText
        The ETag on the ESI return.
    system_id: Unsigned Integer, Primary Key
        The region that the data is for.
    ship_jumps: Unsigned Integer
        The number of outging jumps that have happened within the past hour, given record_time and system_id.
        
    Relationships
    -------------
    system: Jumps.system_id <> System.system_id
    """
    
    __tablename__ = 'uni_Jumps'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    etag = Column(TinyText)
    system_id = Column(Integer(unsigned=True), ForeignKey('map_System.system_id'), primary_key=True, autoincrement=False)
    ship_jumps = Column(Integer(unsigned=True))
    
    ## Relationships
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
                'record_time': dt.strptime(esi_return.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z'),
                'etag': esi_return.headers.get('Etag'),
            }) for data in data_items
        ]
        return class_obj