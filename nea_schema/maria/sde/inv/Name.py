from sqlalchemy import Column
from sqlalchemy.dialects.mysql import \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class Name(Base):
    """ Schema for the inv_Name table
    
    Columns
    -------
    item_id: Unsigned Integer, Primary Key
        Unique identifier for the item name.
    item_name: Tiny Text
        Name for the item.
        
    Relationships
    -------------
    parent_group: MarketGroup.parent_group_id <> MarketGroup.market_group_id
    parent_group: MarketGroup.market_group_id <> MarketGroup.parent_group_id
    type: MarketGroup.group_id <> Type.group_id
    """
    
    __tablename__ = 'inv_Name'
    
    ## Columns
    item_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    item_name = Column(TinyText)

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
            item_id=sde_record.get('itemID'),
            item_name=sde_record.get('itemName'),
        )
        return sde_obj