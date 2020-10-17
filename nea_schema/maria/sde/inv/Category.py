from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class Category(Base):
    """ Schema for the inv_Category table
    
    Columns
    -------
    category_id: Unsigned Integer, Primary Key
        Unique identifier for the category.
    category_name: Tiny Text
        Name for the category.
    icon_id: Unsigned Integer
        Icon for the category.
    published: Boolean
        Whether or not the category is published in the game.
        
    Relationships
    -------------
    group: Category.category_id <> Group.category_id
    """
    
    __tablename__ = 'inv_Category'
    
    ## Columns
    category_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    category_name = Column(TinyText)
    icon_id = Column(Integer(unsigned=True))
    published = Column(Boolean)
    
    ## Relationships
    group = relationship('Group', back_populates='category')

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
            category_id=sde_record.get('categoryID'),
            category_name=sde_record.get('name', {}).get('en'),
            icon_id=sde_record.get('iconID'),
            published=sde_record.get('published'),
        )
        return sde_obj