from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ... import Base

class Group(Base):
    """ Schema for the inv_Group table
    
    Columns
    -------
    group_id: Unsigned Integer, Primary Key
        Unique identifier for the group.
    group_name: Tiny Text
        Name of the group.
    category_id: Unsigned Integer
        Category that the group is in.
    icon_id: Unsigned Integer
        Icon for the group.
    anchorable: Boolean
        ???
    anchored: Boolean
        ???
    fittable_non_singleton: Boolean
        ???
    published: Boolean
        Whether or not the category is published in the game.
    use_base_price: Boolean
        ???
        
    Relationships
    -------------
    category: Group.category_id <> Category.category_id
    type: Group.group_id <> Type.group_id
    """
    
    __tablename__ = 'inv_Group'
    
    ## Columns
    group_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    group_name = Column(TinyText)
    category_id = Column(Integer(unsigned=True), ForeignKey('inv_Category.category_id'))
    icon_id = Column(Integer(unsigned=True))
    anchorable = Column(Boolean)
    anchored = Column(Boolean)
    fittable_non_singleton = Column(Boolean)
    published = Column(Boolean)
    use_base_price = Column(Boolean)
    
    ## Relationships
    category = relationship('Category', back_populates='group')
    type = relationship('Type', back_populates='group')

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
            group_id=sde_record.get('groupID'),
            group_name=sde_record.get('name', {}).get('en'),
            category_id=sde_record.get('categoryID'),
            icon_id=sde_record.get('iconID'),
            anchorable=sde_record.get('anchorable'),
            anchored=sde_record.get('anchored'),
            fittable_non_singleton=sde_record.get('fittableNonSingleton'),
            published=sde_record.get('published'),
            use_base_price=sde_record.get('useBasePrice'),
        )
        return sde_obj