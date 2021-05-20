from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    FLOAT as Float, \
    INTEGER as Integer, \
    TEXT as Text

from ...Base import Base

class DogmaEffect(Base):
    __tablename__ = 'dogma_Effect'
    
    ## Columns
    effect_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    disallow_auto_repeat = Column(Boolean)
    discharge_attribute_id = Column(Integer(unsigned=True))
    duration_attribute_id = Column(Integer(unsigned=True))
    effect_category = Column(Integer(unsigned=True))
    effect_name = Column(Text)
    electronic_chance = Column(Boolean)
    guid = Column(Text)
    is_assistance = Column(Boolean)
    is_offensive = Column(Boolean)
    is_warp_safe = Column(Boolean)
    propulsion_chance = Column(Boolean)
    published = Column(Boolean)
    range_chance = Column(Boolean)
    distribution = Column(Integer(unsigned=True))
    falloff_attribute_id = Column(Integer(unsigned=True))
    range_attribute_id = Column(Integer(unsigned=True))
    tracking_speed_attribute_id = Column(Integer(unsigned=True))
    description = Column(Text)
    display_name = Column(Text)
    icon_id = Column(Integer(unsigned=True))
    npc_usage_chance_attribute_id = Column(Integer(unsigned=True))
    npc_activation_chance_attribute_id = Column(Integer(unsigned=True))
    fitting_usage_chance_attribute_id = Column(Integer(unsigned=True))
    resistance_attribute_id = Column(Integer(unsigned=True))
    
    ## Relationships
    type_effect = relationship('DogmaTypeEffect', back_populates='effect')
    modifier = relationship('DogmaModifier', back_populates='effect')
    
    @classmethod
    def sde_parse(cls, sde_record):
        sde_obj = cls(
            effect_id=sde_record.get('effectID'),
            disallow_auto_repeat=sde_record.get('disallowAutoRepeat'),
            discharge_attribute_id=sde_record.get('dischargeAttributeID'),
            duration_attribute_id=sde_record.get('durationAttributeID'),
            effect_category=sde_record.get('effectCategory'),
            effect_name=sde_record.get('effectName'),
            electronic_chance=sde_record.get('electronicChance'),
            guid=sde_record.get('guid'),
            is_assistance=sde_record.get('isAssistance'),
            is_offensive=sde_record.get('isOffensive'),
            is_warp_safe=sde_record.get('isWarpSafe'),
            propulsion_chance=sde_record.get('propulsionChance'),
            published=sde_record.get('published'),
            range_chance=sde_record.get('rangeChance'),
            distribution=sde_record.get('distribution'),
            falloff_attribute_id=sde_record.get('falloffAttributeID'),
            range_attribute_id=sde_record.get('rangeAttributeID'),
            tracking_speed_attribute_id=sde_record.get('trackingSpeedAttributeID'),
            description=sde_record.get('descriptionID', {}).get('en'),
            display_name=sde_record.get('displayNameID', {}).get('en'),
            icon_id=sde_record.get('iconID'),
            npc_usage_chance_attribute_id=sde_record.get('npcUsageChanceAttributeID'),
            npc_activation_chance_attribute_id=sde_record.get('npcActivationChanceAttributeID'),
            fitting_usage_chance_attribute_id=sde_record.get('fittingUsageChanceAttributeID'),
            resistance_attribute_id=sde_record.get('resistanceAttributeID'),
        )
        return sde_obj
