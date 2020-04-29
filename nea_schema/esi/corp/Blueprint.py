from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYINT as TinyInt, \
    TINYTEXT as TinyText

from ... import Base

class Blueprint(Base):    
    __tablename__ = 'corp_Blueprint'
    
    ## Columns
    record_time = Column(DateTime)
    etag = Column(TinyText)
    item_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    location_id = Column(BigInt)
    material_efficiency = Column(TinyInt(unsigned=True))
    quantity = Column(Integer)
    runs = Column(Integer)
    time_efficiency = Column(TinyInt(unsigned=True))
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    
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
        
        data = esi_return.json()
        class_obj = [cls(**{
            **data,
            'record_time': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag'),
        })]
        return class_obj