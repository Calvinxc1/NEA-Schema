from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class Category(Base):
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
        sde_obj = cls(
            category_id=sde_record.get('categoryID'),
            category_name=sde_record.get('name', {}).get('en'),
            icon_id=sde_record.get('iconID'),
            published=sde_record.get('published'),
        )
        return sde_obj