from sqlalchemy import create_engine

from . import Base

from .esi.srv import *
from .esi.uni import *
from .esi.mkt import *
from .esi.corp import *

from .sde.bp import *
from .sde.inv import *
from .sde.map import *

def build_schema(sql_params):
    """ Initializes the schema in the database
    
    Note: Importing all of the applicable schema is necessary to initialize properly
    
    Parameters
    ----------
    sql_params: dict
        Contains all of the SQL URL parameters for the SQL connection.
        
    Returns: None
    """
    
    engine = create_engine('{engine}://{user}:{passwd}@{host}/{db}'.format(**sql_params))
    Base.metadata.create_all(engine)