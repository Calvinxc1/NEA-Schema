from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    INTEGER as Integer

from ... import Base

class Reprocess(Base):
    """ Schema for the inv_Reprocess table
    
    Columns
    -------
    type_id: Unsigned Integer, Primary Key
        Type of reprocessed item.
    material_type_id: Unsigned Integer, Primary Key
        Type of resulting item from reprocessing type_id.
    quantity: Unsigned Integer
        Raw 100% quantity of material_type_id of reprocessing type_id.
        
    Relationships
    -------------
    type: Reprocess.group_id <> Type.type_id
    material_type: Reprocess.material_type_id <> Type.type_id
    """
    
    __tablename__ = 'inv_Reprocess'
    
    ## Columns
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id', ondelete='CASCADE'), primary_key=True, autoincrement=False)
    material_type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id', ondelete='CASCADE'), primary_key=True, autoincrement=False)
    quantity = Column(Integer(unsigned=True))
    
    ## Relationships
    type = relationship('Type', foreign_keys='Reprocess.type_id')
    material_type = relationship('Type', foreign_keys='Reprocess.material_type_id')

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
            type_id=sde_record.get('typeID'),
            material_type_id=sde_record.get('materialTypeID'),
            quantity=sde_record.get('quantity'),
        )
        return sde_obj