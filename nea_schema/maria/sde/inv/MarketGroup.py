from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    INTEGER as Integer, \
    TEXT as Text, \
    TINYTEXT as TinyText

from ...Base import Base

class MarketGroup(Base):
    """ Schema for the inv_MarketGroup table
    
    Columns
    -------
    market_group_id: Unsigned Integer, Primary Key
        Unique identifier for the market group.
    market_group_name: Tiny Text
        Name of the market group.
    market_group_desc: Text
        Long description for the market group.
    parent_group_id: Unsigned Integer
        Parent market group.
    icon_id: Unsigned Integer
        Icon for market group.
    has_types: Boolean
        Whether or not the market group has types associated with it.
        
    Relationships
    -------------
    parent_group: MarketGroup.parent_group_id <> MarketGroup.market_group_id
    parent_group: MarketGroup.market_group_id <> MarketGroup.parent_group_id
    type: MarketGroup.group_id <> Type.group_id
    """
    
    __tablename__ = 'inv_MarketGroup'
    
    ## Columns
    market_group_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    market_group_name = Column(TinyText)
    market_group_desc = Column(Text)
    parent_group_id = Column(Integer(unsigned=True), ForeignKey('inv_MarketGroup.market_group_id'))
    icon_id = Column(Integer(unsigned=True))
    has_types = Column(Boolean)
    
    ## Relationships
    parent_group = relationship('MarketGroup', remote_side=[market_group_id], viewonly=True)
    child_group = relationship('MarketGroup', remote_side=[parent_group_id], viewonly=True)
    type = relationship('Type')

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
        
        try:
            sde_obj = cls(
                market_group_id=sde_record.get('marketGroupID'),
                market_group_name=sde_record.get('nameID', {}).get('en'),
                market_group_desc=sde_record.get('descriptionID', {}).get('en'),
                parent_group_id=sde_record.get('parentGroupID'),
                icon_id=sde_record.get('iconID'),
                has_types=sde_record.get('hasTypes'),
            )
        except Exception as e:
            print(sde_record)
            raise Exception(e)
        return sde_obj