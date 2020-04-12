from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import \
    DATETIME as DateTime, \
    INTEGER as Integer

from ... import Base

class Kills(Base):
    __tablename__ = 'map_Kills'
    
    ## Columns
    record_time = Column(DateTime, primary_key=True, autoincrement=False)
    system_id = Column(Integer(unsigned=True), ForeignKey('map_System.system_id'), primary_key=True, autoincrement=False)
    npc_kills = Column(Integer(unsigned=True))
    ship_kills = Column(Integer(unsigned=True))
    pod_kills = Column(Integer(unsigned=True))

    @classmethod
    def esi_parse(cls, esi_return):
        data_items = esi_return.json()
        class_obj = [
            cls(**{
                **data,
                'record_time': dt.strptime(esi_return.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z'),
            }) for data in data_items
        ]
        return class_obj