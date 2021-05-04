from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    FLOAT as Float, \
    INTEGER as Integer, \
    TEXT as Text

from ...Base import Base

class DogmaModifier(Base):
    """ Schema for the DogmaModifier table
    
    Columns
    -------
    parent_effect_id: Unsigned Integer
        The effect the modifier is associated with
    domain: Text
        The domain of infleunce of the modifier
    func: Text
        The function of the domain
    modified_attribute_id: Unsgined Integer
        The attribute modified by the modifier
    modifying_attribute_id: Unsigned Integer
        The attrubite doing the modifying by the modifier
    operation: Signed Integer
        ???
    group_id: Unsigned Integer
        ???
    skill_type_id: Unsigned Integer
        ???
    effect_id: Unsigned Integer
        ???
        
    Relationships
    -------------
    parent_effect: DogmaModifier.parent_effect_id <> DogmaEffect.effect_id
    """
    
    __tablename__ = 'dogma_Modifier'
    
    ## columns
    modifier_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=True)
    parent_effect_id = Column(Integer(unsigned=True), ForeignKey('dogma_Effect.effect_id'))
    domain = Column(Text)
    func = Column(Text)
    modified_attribute_id = Column(Integer(unsigned=True))
    modifying_attribute_id = Column(Integer(unsigned=True))
    operation = Column(Integer(unsigned=False))
    group_id = Column(Integer(unsigned=True))
    skill_type_id = Column(Integer(unsigned=True))
    effect_id = Column(Integer(unsigned=True))
    
    ## Relationships
    effect = relationship('DogmaEffect', back_populates='modifier')
    
    @classmethod
    def sde_parse(cls, sde_record):
        sde_obj = cls(
            parent_effect_id=sde_record.get('parent_effect_id'),
            domain=sde_record.get('domain'),
            func=sde_record.get('func'),
            modified_attribute_id=sde_record.get('modifiedAttributeID'),
            modifying_attribute_id=sde_record.get('modifyingAttributeID'),
            operation=sde_record.get('operation'),
            group_id=sde_record.get('groupID'),
            skill_type_id=sde_record.get('skillTypeID'),
            effect_id=sde_record.get('effectID'),
        )
        return sde_obj
