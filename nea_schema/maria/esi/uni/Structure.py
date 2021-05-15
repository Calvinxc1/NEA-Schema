from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    BIGINT as BigInt, \
    INTEGER as Integer, \
    TINYTEXT as TinyText, \
    DOUBLE as Double

from ...Base import Base

class Structure(Base):
    __tablename__ = 'uni_Structure'
    
    ## Columns
    record_time = Column(DateTime)
    etag = Column(TinyText)
    structure_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    structure_name = Column(TinyText)
    owner_id = Column(Integer(unsigned=True))
    system_id = Column(Integer(unsigned=True), ForeignKey('map_System.system_id'))
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    pos_x = Column(Double(unsigned=False))
    pos_y = Column(Double(unsigned=False))
    pos_z = Column(Double(unsigned=False))    
    
    ## Relationships
    system = relationship('System')
    type = relationship('Type')

    @classmethod
    def esi_parse(cls, esi_return, orm=True):
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        etag = esi_return.headers.get('Etag')
        structure_id = int(esi_return.url.split('?')[0].split('/')[-1])
        row = esi_return.json()
        record_items = [{
            'record_time': record_time,
            'etag': etag,
            'structure_name': row.pop('name'),
            'system_id': row.pop('solar_system_id'),
            **{'pos_{}'.format(key):val for key, val in row.pop('position').items()},
            **row,
            'structure_id': structure_id,
        }]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
