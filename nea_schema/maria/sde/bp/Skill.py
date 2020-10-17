from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    INTEGER as Integer, \
    VARCHAR as VarChar

from ...Base import Base
from . import Activity

class Skill(Base):
    __tablename__ = 'bp_Skill'
    
    ## Columns
    blueprint_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    activity_type = Column(VarChar(length=17), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id', ondelete='CASCADE'), primary_key=True, autoincrement=False)
    level = Column(Integer(unsigned=True))
    
    ## Foreign Key Constraint
    __table_args__ = (
        ForeignKeyConstraint(
            [blueprint_id, activity_type],
            [Activity.blueprint_id, Activity.activity_type],
            ondelete='CASCADE',
        ),
        {},
    )
    
    ## Relationships
    activity = relationship('Activity', back_populates='skill')
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
        
        sde_obj = cls(
            blueprint_id=sde_record.get('blueprintID'),
            activity_type=sde_record.get('activity_type'),
            type_id=sde_record.get('typeID'),
            level=sde_record.get('level'),
        )
        return sde_obj