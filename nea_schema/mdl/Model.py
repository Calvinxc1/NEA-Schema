from datetime import datetime as dt
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    INTEGER as Integer, \
    TEXT as Text, \
    TINYTEXT as TinyText

from ... import Base

class Model(Base):
    __tablename__ = 'mdl_Model'
    
    ## Columns
    model_id = Column(Integer, primary_key=True)
    model_name = Column(TinyText)
    model_desc = Column(Text)
    enabled = Column(Boolean)