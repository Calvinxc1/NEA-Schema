from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import DOUBLE as Double, INTEGER as Integer
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from ... import Base

class Region(Base):
    """ Schema for the map_Region table
    
    Columns
    -------
    region_id: Unsigned Integer, Primary Key
        The unique identifier for the region.
    name_id: Unsigned Integer
        Name ID number.
    desc_id: Unsigned Integer
        Description ID number.
    faction_id: Unsigned Integer
        Faction ID number.
    nebula: Unsigned Integer
        Unique nebula ID.
    wormhole_class_id: Unsigned Integer
        Wormhole Class ID.
    min_x/y/z: Signed Double
        XYZ vector for the region's min coordinates in the universe frame.
    center_x/y/z: Signed Double
        XYZ vector for the region's origin coordinates in the universe frame.
    max_x/y/z: Signed Double
        XYZ vector for the region's max coordinates in the universe frame.
        
    Relationships
    -------------
    name: Region.region_id <> Name.item_id
    constellation: Region.region_id <> Constellation.region_id
    """
    
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
        """ Auto-parser for EVE Static Data Export file(s)
        
        Parameters
        ----------
        sde_record: dict
            YAML-parsed dictionary of a specific region
            
        Returns
        -------
        Region:
            A fully-populated Region object
        """
        
        sde_obj = cls(
            region_id=sde_record.get('regionID'),
            name_id=sde_record.get('nameID'),
            desc_id=sde_record.get('descriptionID'),
            faction_id=sde_record.get('factionID'),
            nebula=sde_record.get('nebula'),
            wormhole_class_id=sde_record.get('wormholeClassID'),
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