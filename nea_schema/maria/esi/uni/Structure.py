from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    BIGINT as BigInt, \
    INTEGER as Integer, \
    TINYTEXT as TinyText, \
    DOUBLE as Double

from ...Base import Base

class Structure(Base):
    """ Schema for the uni_Jumps table
    
    Columns
    -------
    record_time: DateTime, Primary Key
        The cache time on the ESI return.
    etag: TinyText
        The ETag on the ESI return.
    system_id: Unsigned Integer, Primary Key
        The region that the data is for.
    ship_jumps: Unsigned Integer
        The number of outging jumps that have happened within the past hour, given record_time and system_id.
        
    Relationships
    -------------
    system: Jumps.system_id <> System.system_id
    """
    
    __tablename__ = 'uni_Structure'
    
    ## Columns
    record_time = Column(DateTime)
    etag = Column(TinyText)
    structure_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    structure_name = Column(TinyText)
    owner_id = Column(Integer(unsigned=True))
    system_id = Column(Integer(unsigned=True), ForeignKey('map_System.system_id'))
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    pos_x = Column(Double(unsigned=False))
    pos_y = Column(Double(unsigned=False))
    pos_z = Column(Double(unsigned=False))    
    
    ## Relationships
    system = relationship('System')
    type = relationship('Type')

    @classmethod
    def esi_parse(cls, esi_return):
        """ Parses and returns an ESI record
        
        Parses through a Requests return, returning a copy of the initialized class.
        
        Parameters
        ----------
        esi_return: Requests return
            A Requests return from an ESI endpoint.
            
        Returns
        -------
        class_obj: class
            An initialized copy of the class.
        """
        
        data_items = esi_return.json()
        class_obj = [cls(
                record_time=dt.strptime(esi_return.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z'),
                etag=esi_return.headers.get('Etag'),
                structure_id=int(esi_return.url.split('/')[-1]),
                structure_name=data_items['name'],
                owner_id=data_items['owner_id'],
                system_id=data_items['solar_system_id'],
                type_id=data_items['type_id'],
                pos_x=data_items['position']['x'],
                pos_y=data_items['position']['y'],
                pos_z=data_items['position']['z'],
        )]
        return class_obj