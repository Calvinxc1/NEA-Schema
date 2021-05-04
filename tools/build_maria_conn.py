from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def build_maria_conn(sql_params, fk_override=True):
    engine = create_engine('{engine}://{user}:{passwd}@{host}/{db}'.format(**sql_params))
    session = sessionmaker(bind=engine)
    conn = session()
    if fk_override: conn.execute('SET SESSION foreign_key_checks=0;')
    return conn
