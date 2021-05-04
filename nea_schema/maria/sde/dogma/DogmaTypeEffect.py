from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    INTEGER as Integer

from ...Base import Base

class DogmaTypeEffect(Base):
    """ Schema for the DogpaTypeEffect table
    
    Columns
    -------
    type_id: Unsigned Integer, Primary Key
        The type item that the dogma attribute applies to.
    effect_id: Unsigned Integer, Primary Key
        The effect that is being applied to the type.
    is_default: Boolean
        ???
        
    Relationships
    -------------
    type: DogmaTypeAttribute.type_id <> Type.type_id
    attribute: DogmaTypeAttribute.attribute_id <> DogmaAttribute.attribute_id
    """
    
    __tablename__ = 'dogma_TypeEffect'
    
    ## Columns
    type_id = Column(
        Integer(unsigned=True), ForeignKey('inv_Type.type_id'),
        primary_key=True, autoincrement=False
    )
    effect_id = Column(
        Integer(unsigned=True), ForeignKey('dogma_Effect.effect_id'),
        primary_key=True, autoincrement=False,
    )
    is_default = Column(Boolean)
    
    type = relationship('Type', back_populates='type_effect')
    effect = relationship('DogmaEffect', back_populates='type_effect')
    
    @classmethod
    def sde_parse(cls, sde_record):
        sde_obj = [cls(
            type_id=sde_record.get('type_id'),
            effect_id=attr_item.get('effectID'),
            is_default=attr_item.get('isDefault'),
        ) for attr_item in sde_record['dogmaEffects']]
        return sde_obj
