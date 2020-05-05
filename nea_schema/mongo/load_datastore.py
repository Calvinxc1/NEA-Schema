from ming import configure

def load_datastore(mongo_params):
    uri = 'mongodb://{username}:{password}@{host}:27017/{database}'.format(**mongo_params)
    configure(ming={mongo_params['database']: {'uri': uri}})