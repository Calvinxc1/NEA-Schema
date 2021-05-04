from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    DOUBLE as Double, \
    FLOAT as Float, \
    INTEGER as Integer, \
    TEXT as Text, \
    TINYTEXT as TinyText

from ...Base import Base

class Type(Base):
    """ Schema for the inv_Type table
    
    Columns
    -------
    type_id: Unsigned Integer, Primary Key
        Unique identifier for type.
    type_name: Tiny Text
        Name of type.
    type_desc: Text
        Description of type.
    group_id: Unsigned Integer
        Group that type is a part of.
    market_group_id: Unisgned Integer
        Market Group that type is a part of.
    faction_id: Unsigned Integer
        Faction that type is a part of (???).
    graphic_id: Unsigned Integer
        Graphic that type is a part of.
    icon_id: Unsinged Integer
        Icon that type is a part of.
    meta_group_id: Unsigned Integer
        ???
    sound_id: Unsigned Integer
        ???
    race_id: Unsigned Integer
        ???
    variation_parent_type_id: Unsigned Integer
        ???
    base_price: Unsigned Float
        ???
    capacity: Unsgined Float
        ???
    mass: Unsigned Double
        Amount of mass (packaged/unpackaged?) the item has.
    portion_size: Unsigned Integer
        How many units are required to reprocess/refine the item.
    published: Boolean
        Whether or not the category is published in the game.
    radius: Unsigned Float
        The in-space radius size of the object.
    volume: Unsigned Float
        How much (packaged/unpackaged?) volume the item takes up.
    sof_faction_name: Tiny Text
        ???
    sof_material_set_id: Unsigned Integer
        ???
        
    Relationships
    -------------
    group: Type.group_id <> Group.group_id
    market_group: Type.market_group_id <> MarketGroup.market_group_id
    type_attribute: Type.type_id <> DogmaTypeAttribute.type_id
    type_effect: Type.type_id <> DogmaTypeEffect.type_id
    """
    
    __tablename__ = 'inv_Type'
    
    ## Columns
    type_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    type_name = Column(TinyText)
    type_desc = Column(Text)
    group_id = Column(Integer(unsigned=True), ForeignKey('inv_Group.group_id'))
    market_group_id = Column(Integer(unsigned=True), ForeignKey('inv_MarketGroup.market_group_id'))
    faction_id = Column(Integer(unsigned=True))
    graphic_id = Column(Integer(unsigned=True))
    icon_id = Column(Integer(unsigned=True))
    meta_group_id = Column(Integer(unsigned=True))
    sound_id = Column(Integer(unsigned=True))
    race_id = Column(Integer(unsigned=True))
    variation_parent_type_id = Column(Integer(unsigned=True))
    base_price = Column(Float(unsigned=True))
    capacity = Column(Float(unsigned=True))
    mass = Column(Double(unsigned=True))
    portion_size = Column(Integer(unsigned=True))
    published = Column(Boolean)
    radius = Column(Float(unsigned=True))
    volume = Column(Float(unsigned=True))
    sof_faction_name = Column(TinyText)
    sof_material_set_id = Column(Integer(unsigned=True))
    
    ## Relationships
    group = relationship('Group', back_populates='type')
    market_group = relationship('MarketGroup', back_populates='type')
    type_attribute = relationship('DogmaTypeAttribute', back_populates='type')
    type_effect = relationship('DogmaTypeEffect', back_populates='type')

    @classmethod
    def sde_parse(cls, sde_record):
        """ Parses and returns an SDE record.
        
        Parses through a PyYAML processed SDE record, returning a copy of the initialized class.
        
        Parameters
        ----------
        sde_record: dict
            Dictionary of PyYAML parsed SDE record.
            
        Returns
        -------
        sde_obj: class
            An initialized copy of the class.
        """
        
        sde_obj = cls(
            type_id=sde_record.get('typeID'),
            type_name=sde_record.get('name', {}).get('en'),
            type_desc=sde_record.get('description', {}).get('en'),
            group_id=sde_record.get('groupID'),
            market_group_id=sde_record.get('marketGroupID'),
            faction_id=sde_record.get('factionID'),
            graphic_id=sde_record.get('graphicID'),
            icon_id=sde_record.get('iconID'),
            meta_group_id=sde_record.get('metaGroupID'),
            sound_id=sde_record.get('soundID'),
            race_id=sde_record.get('raceID'),
            variation_parent_type_id=sde_record.get('variationParentTypeID'),
            base_price=sde_record.get('basePrice'),
            capacity=sde_record.get('capacity'),
            mass=sde_record.get('mass'),
            portion_size=sde_record.get('portionSize'),
            published=sde_record.get('published'),
            radius=sde_record.get('radius'),
            volume=sde_record.get('volume'),
            sof_faction_name=sde_record.get('sofFactionName'),
            sof_material_set_id=sde_record.get('sofMaterialSetID'),
        )
        return sde_obj