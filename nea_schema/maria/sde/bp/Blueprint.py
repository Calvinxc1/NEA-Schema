from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    INTEGER as Integer

from ... import Base

class Blueprint(Base):
    __tablename__ = 'bp_Blueprint'
    
    ## Columns
    blueprint_id = Column(Integer(unsigned=True), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id', ondelete='CASCADE'))
    max_production_limit = Column(Integer(unsigned=True))
    
    ## Relationships
    type = relationship('Type')
    activity = relationship('Activity', back_populates='blueprint')
    
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
            type_id=sde_record.get('blueprintTypeID'),
            max_production_limit=sde_record.get('maxProductionLimit'),
        )
        return sde_obj