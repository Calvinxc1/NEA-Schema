from sqlalchemy import create_engine

from . import Base
from .esi.status import *
from .sde.bp import *
from .sde.inv import *
from .sde.map import *

def build_schema(sql_params):
    engine = create_engine('{engine}://{user}:{passwd}@{host}/{db}'.format(**sql_params))
    Base.metadata.create_all(engine)