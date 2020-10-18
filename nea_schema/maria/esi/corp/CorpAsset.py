from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    BOOLEAN as Boolean, \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYINT as TinyInt, \
    TINYTEXT as TinyText

from ...Base import Base

class CorpAsset(Base):    
    __tablename__ = 'corp_Asset'
    
    ## Columns
    record_time = Column(DateTime)
    etag = Column(TinyText)
    is_blueprint_copy = Column(Boolean)
    is_singleton = Column(Boolean)
    item_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    item_name = Column(TinyText)
    location_flag = Column(TinyText)
    location_id = Column(BigInt)
    location_type = Column(TinyText)
    quantity = Column(Integer)
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
        
        class_obj = [cls(**{
            **data,
            'record_time': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag'),
        }) for data in esi_return.json()]
        return class_obj