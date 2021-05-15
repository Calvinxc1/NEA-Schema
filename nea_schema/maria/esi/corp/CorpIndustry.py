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
    def esi_parse(cls, esi_return, orm=True):
        activity_lookup = {
            1: 'manufacturing',
            3: 'research_time',
            4: 'research_material',
            5: 'copying',
            8: 'invention',
        }
        
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        etag = esi_return.headers.get('Etag')
        record_items = [{
            'record_time': record_time,
            'etag': etag,
            'activity_type': activity_lookup.get(row.pop('activity_id')),
            **row,
            'completed_date': None if row.get('completed_date') is None\
                else dt.strptime(row.get('completed_date'), '%Y-%m-%dT%H:%M:%SZ'),
            'end_date': dt.strptime(row.get('end_date'), '%Y-%m-%dT%H:%M:%SZ'),
            'pause_date': None if row.get('pause_date') is None\
                else dt.strptime(row.get('pause_date'), '%Y-%m-%dT%H:%M:%SZ'),
            'start_date': dt.strptime(row.get('start_date'), '%Y-%m-%dT%H:%M:%SZ'),
        } for row in esi_return.json()]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
