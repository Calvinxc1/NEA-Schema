from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    FLOAT as Float, \
    INTEGER as Integer

from ...Base import Base

class DogmaTypeAttribute(Base):
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
