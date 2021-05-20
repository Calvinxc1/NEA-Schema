from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    FLOAT as Float, \
    INTEGER as Integer, \
    TEXT as Text

from ...Base import Base

class DogmaAttribute(Base):
    __tablename__ = 'dogma_Attribute'
    
    ## Columns
    attribute_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    category_id = Column(Integer(unsigned=True), ForeignKey('dogma_Category.category_id'))
    data_type = Column(Integer(unsigned=True))
    default_value = Column(Float)
    description = Column(Text)
    high_is_good = Column(Boolean)
    name = Column(Text)
    published = Column(Boolean)
    stackable = Column(Boolean)
    display_name = Column(Text)
    icon_id = Column(Integer(unsigned=True))
    tooltip_description = Column(Text)
    tooltip_title = Column(Text)
    unit_id = Column(Integer(unsigned=True))
    charge_recharge_time_id = Column(Integer(unsigned=True))
    max_attribute_id = Column(Integer(unsigned=True))
    
    ## Relationships
    category = relationship('DogmaCategory', back_populates='attribute')
    type_attribute = relationship('DogmaTypeAttribute', back_populates='attribute')
    
    @classmethod
    def sde_parse(cls, sde_record):
        sde_obj = cls(
            attribute_id=sde_record.get('attributeID'),
            category_id=sde_record.get('categoryID'),
            data_type=sde_record.get('dataType'),
            default_value=sde_record.get('defaultValue'),
            description=sde_record.get('description'),
            high_is_good=sde_record.get('highIsGood'),
            name=sde_record.get('name'),
            published=sde_record.get('published'),
            stackable=sde_record.get('stackable'),
            display_name=sde_record.get('displayNameID', {}).get('en'),
            icon_id=sde_record.get('iconID'),
            tooltip_description=sde_record.get('tooltipDescriptionID', {}).get('en'),
            tooltip_title=sde_record.get('tooltipTitleID', {}).get('en'),
            unit_id=sde_record.get('unitID'),
            charge_recharge_time_id=sde_record.get('chargeRechargeTimeID'),
            max_attribute_id=sde_record.get('maxAttributeID'),
        )
        return sde_obj
