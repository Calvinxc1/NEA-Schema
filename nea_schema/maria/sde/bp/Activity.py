from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    INTEGER as Integer, \
    VARCHAR as VarChar

from ...Base import Base

class Activity(Base):
    __tablename__ = 'bp_Activity'
    
    ## Columns
    blueprint_id = Column(Integer(unsigned=True), ForeignKey('bp_Blueprint.blueprint_id', ondelete='CASCADE'), primary_key=True, autoincrement=False)
    activity_type = Column(VarChar(length=17), primary_key=True, autoincrement=False)
    time = Column(Integer(unsigned=True))
    
    ## Relationships
    blueprint = relationship('Blueprint', back_populates='activity')
    material = relationship('Material', back_populates='activity')
    product = relationship('Product', back_populates='activity')
    skill = relationship('Skill', back_populates='activity')
    
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
            blueprint_id=sde_record.get('blueprintID'),
            activity_type=sde_record.get('activity_type'),
            time=sde_record.get('time'),
        )
        return sde_obj