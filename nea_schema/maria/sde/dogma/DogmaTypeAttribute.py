from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    FLOAT as Float, \
    INTEGER as Integer

from ...Base import Base

class DogmaTypeAttribute(Base):
    """ Schema for the DogpaTypeAttribute table
    
    Columns
    -------
    type_id: Unsigned Integer, Primary Key
        The type item that the dogma attribute applies to.
    attribute_id: Unsigned Integer, Primary Key
        The attribute that is being applied to the type.
    value: Signed Float
        The value being applied to the type's attribute
        
    Relationships
    -------------
    type: DogmaTypeAttribute.type_id <> Type.type_id
    attribute: DogmaTypeAttribute.attribute_id <> DogmaAttribute.attribute_id
    """
    
    __tablename__ = 'dogma_TypeAttribute'
    
    ## Columns
    type_id = Column(
        Integer(unsigned=True), ForeignKey('inv_Type.type_id'),
        primary_key=True, autoincrement=False
    )
    attribute_id = Column(
        Integer(unsigned=True), ForeignKey('dogma_Attribute.attribute_id'),
        primary_key=True, autoincrement=False,
    )
    value = Column(Float)
    
    type = relationship('Type', back_populates='type_attribute')
    attribute = relationship('DogmaAttribute', back_populates='type_attribute')
    
    @classmethod
    def sde_parse(cls, sde_record):
        sde_obj = [cls(
            type_id=sde_record.get('type_id'),
            attribute_id=attr_item.get('attributeID'),
            value=attr_item.get('value'),
        ) for attr_item in sde_record['dogmaAttributes']]
        return sde_obj
