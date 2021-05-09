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
    activity_type = Column(TinyText)
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
    product = relationship('Product', primaryjoin="""and_(
                            CorpIndustry.blueprint_type_id == foreign(Product.blueprint_id),
                            CorpIndustry.activity_type == foreign(Product.activity_type),
                            CorpIndustry.product_type_id == foreign(Product.type_id),
                            )""", viewonly=True, uselist=False)
    output_type = relationship('Type', foreign_keys=[product_type_id])
    blueprint = relationship('CorpBlueprint', primaryjoin='CorpIndustry.blueprint_id == foreign(CorpBlueprint.item_id)', viewonly=True, uselist=False)
    

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
        
        activity_lookup = {
            1: 'manufacturing',
            3: 'research_time',
            4: 'research_material',
            5: 'copying',
            8: 'invention',
        }
        
        class_obj = [cls(**{
            'activity_type': activity_lookup.get(data.get('activity_id')),
            'blueprint_id': data.get('blueprint_id'),
            'blueprint_location_id': data.get('blueprint_location_id'),
            'blueprint_type_id': data.get('blueprint_type_id'),
            'completed_character_id': data.get('completed_character_id'),
            'completed_date': None if data.get('completed_date') is None\
                else dt.strptime(data.get('completed_date'), '%Y-%m-%dT%H:%M:%SZ'),
            'cost': data.get('cost'),
            'duration': data.get('duration'),
            'end_date': dt.strptime(data.get('end_date'), '%Y-%m-%dT%H:%M:%SZ'),
            'facility_id': data.get('facility_id'),
            'installer_id': data.get('installer_id'),
            'job_id': data.get('job_id'),
            'licensed_runs': data.get('licensed_runs'),
            'location_id': data.get('location_id'),
            'output_location_id': data.get('output_location_id'),
            'pause_date': None if data.get('pause_date') is None\
                else dt.strptime(data.get('pause_date'), '%Y-%m-%dT%H:%M:%SZ'),
            'probability': data.get('probability'),
            'product_type_id': data.get('product_type_id'),
            'runs': data.get('runs'),
            'start_date': dt.strptime(data.get('start_date'), '%Y-%m-%dT%H:%M:%SZ'),
            'status': data.get('status'),
            'successful_runs': data.get('successful_runs'),
            'record_time': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag'),
        }) for data in esi_return.json()]
        return class_obj
