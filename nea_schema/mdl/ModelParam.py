from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    INTEGER as Integer, \
    TEXT as Text, \
    TINYTEXT as TinyText

from ... import Base

class Model(Base):
    __tablename__ = 'mdl_ModelParam'
    
    ## Columns
    model_param_id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('mdl_Model.model_id'))
    param_type = Column(TinyText)
    value = Column(Text)