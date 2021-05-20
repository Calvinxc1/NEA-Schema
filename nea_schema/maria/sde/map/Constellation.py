from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.dialects.mysql import \
    INTEGER as Integer, \
    DOUBLE as Double

from ...Base import Base

class Constellation(Base):
    __tablename__ = 'map_Constellation'
    
    ## Columns
    constellation_id = Column(Integer(unsigned=True), ForeignKey('inv_Name.item_id'), primary_key=True, autoincrement=False)
    region_id = Column(Integer(unsigned=True), ForeignKey('map_Region.region_id'))
    name_id = Column(Integer(unsigned=True))
    faction_id = Column(Integer(unsigned=True))
    wormhole_class_id = Column(Integer(unsigned=True))
    radius = Column(Double(unsigned=False))
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
    region = relationship('Region', back_populates='constellation')
    system = relationship('System', back_populates='constellation')
    
    ## Aliased Columns
    constellation_name = association_proxy('item_name', 'item_name')
    
    @classmethod
    def sde_parse(cls, sde_record):
        sde_obj = cls(
            constellation_id=sde_record.get('constellationID'),
            region_id=sde_record.get('regionID'),
            name_id=sde_record.get('nameID'),
            faction_id=sde_record.get('factionID'),
            wormhole_class_id=sde_record.get('wormholeClassID'),
            radius=sde_record.get('radius'),
            min_x=sde_record.get('min', [None, None, None])[0],
            min_y=sde_record.get('min', [None, None, None])[1],
            min_z=sde_record.get('min', [None, None, None])[2],
            center_x=sde_record.get('center', [None, None, None])[0],
            center_y=sde_record.get('center', [None, None, None])[1],
            center_z=sde_record.get('center', [None, None, None])[2],
            max_x=sde_record.get('max', [None, None, None])[0],
            max_y=sde_record.get('max', [None, None, None])[1],
            max_z=sde_record.get('max', [None, None, None])[2],
        )
        return sde_obj