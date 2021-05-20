from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    DOUBLE as Double, \
    INTEGER as Integer

from ...Base import Base

class Region(Base):
    __tablename__ = 'map_Region'
    
    ## Columns
    region_id = Column(Integer(unsigned=True), ForeignKey('inv_Name.item_id'), primary_key=True, autoincrement=False)
    name_id = Column(Integer(unsigned=True))
    desc_id = Column(Integer(unsigned=True))
    faction_id = Column(Integer(unsigned=True))
    nebula = Column(Integer(unsigned=True))
    wormhole_class_id = Column(Integer(unsigned=True))
    min_x = Column(Double(unsigned=False))
    min_y = Column(Double(unsigned=False))
    min_z = Column(Double(unsigned=False))
    center_x = Column(Double(unsigned=False))
    center_y = Column(Double(unsigned=False))
    center_z = Column(Double(unsigned=False))
    max_x = Column(Double(unsigned=False))
    max_y = Column(Double(unsigned=False))
    max_z = Column(Double(unsigned=False))
    
    ## Relationships
    name = relationship('Name')
    constellation = relationship('Constellation', back_populates='region')
    
    @classmethod
    def sde_parse(cls, sde_record):
        sde_obj = cls(
            region_id=sde_record.get('regionID'),
            name_id=sde_record.get('nameID'),
            desc_id=sde_record.get('descriptionID'),
            faction_id=sde_record.get('factionID'),
            nebula=sde_record.get('nebula'),
            wormhole_class_id=sde_record.get('wormholeClassID'),
            **{'min_{}'.format(dim):val for dim, val in zip(['x', 'y', 'z'], sde_record.get('min', [None]*3))},
            **{'center_{}'.format(dim):val for dim, val in zip(['x', 'y', 'z'], sde_record.get('center', [None]*3))},
            **{'max_{}'.format(dim):val for dim, val in zip(['x', 'y', 'z'], sde_record.get('max', [None]*3))},
        )
        return sde_obj