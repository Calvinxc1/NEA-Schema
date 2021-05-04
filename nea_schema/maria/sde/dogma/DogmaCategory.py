from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    INTEGER as Integer, \
    TEXT as Text

from ...Base import Base

class DogmaCategory(Base):
    """ Schema for the DogmaCategory table
    
    Columns
    -------
    category_id: Unsigned Integer
        The id for the category
    description: Text
        The description of the category
    name: Text
        The name of the category
        
    Relationships:
    --------------
    attribute: DogmaCategory.category_id <> DogmaAttribute.category_id
    """
    
    __tablename__ = 'dogma_Category'
    
    ## Columns
    category_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    description = Column(Text)
    name = Column(Text)
    
    ## Relationships
    attribute = relationship('DogmaAttribute', back_populates='category')
    
    @classmethod
    def sde_parse(cls, sde_record):
        sde_obj = cls(
            category_id=sde_record.get('category_id'),
            description=sde_record.get('description'),
            name=sde_record.get('name'),
        )
        return sde_obj
