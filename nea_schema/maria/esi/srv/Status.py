from datetime import datetime as dt
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import \
    BOOLEAN as Boolean, \
    DATETIME as DateTime, \
    INTEGER as Integer, \
    TINYTEXT as TinyText

from ...Base import Base

class Status(Base):
    """ Schema for the srv_ServerStatus table
    
    Columns
    -------
    record_time: DateTime, Primary Key
        The cache time on the ESI return
    etag: TinyText
        The ETag on the ESI return
    players: Unsigned Integer
        Number of players logged into the server, as of record_time
    server_version: TinyText
        What version the server is in, as ofrecord_time
    start_time: DateTime
        When the server was last started after downtime, as of record_time
    vip: Boolean
        If the server is in VIP mode, as of record_time
    """
    
    __tablename__ = 'srv_ServerStatus'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    etag = Column(TinyText)
    players = Column(Integer(unsigned=True))
    server_version = Column(TinyText)
    start_time = Column(DateTime)
    vip = Column(Boolean, default=False)

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
        
        data = esi_return.json()
        class_obj = [cls(**{
            **data,
            'start_time': dt.strptime(data['start_time'], '%Y-%m-%dT%H:%M:%SZ'),
            'record_time': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag'),
        })]
        return class_obj