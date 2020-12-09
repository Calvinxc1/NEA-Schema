from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYINT as TinyInt, \
    TINYTEXT as TinyText, \
    DOUBLE as Double, \
    FLOAT as Float

from ...Base import Base

class CorpIndustry(Base):    
    __tablename__ = 'corp_Industry'
    
    ## Columns
    record_time = Column(DateTime)
    etag = Column(TinyText)
    activity_id = Column(Integer(unsigned=True))
    blueprint_id = Column(BigInt(unsigned=True))
    blueprint_location_id = Column(BigInt(unsigned=True))
    blueprint_type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    completed_character_id = Column(BigInt(unsigned=True))
    completed_date = Column(DateTime)
    cost = Column(Double(unsigned=True))
    duration = Column(Integer(unsigned=True))
    end_date = Column(DateTime)
    facility_id = Column(BigInt(unsigned=True))
    installer_id = Column(BigInt(unsigned=True))
    job_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    licensed_runs = Column(Integer(unsigned=True))
    location_id = Column(BigInt(unsigned=True))
    output_location_id = Column(BigInt(unsigned=True))
    pause_date = Column(DateTime)
    probability = Column(Float(unsigned=True))
    product_type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    runs = Column(Integer(unsigned=True))
    start_date = Column(DateTime)
    status = Column(TinyText)
    successful_runs = Column(Integer(unsigned=True))
    
    ## Relationships
    bp_type = relationship('Type', foreign_keys=[blueprint_type_id])
    output_type = relationship('Type', foreign_keys=[product_type_id])

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
