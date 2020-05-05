from ming.odm import ODMSession, ThreadLocalODMSession

def session(datastore_name, thread_local=True):
    if thread_local:
        return ThreadLocalODMSession.by_name(datastore_name)
    else:
        return ODMSession.by_name(datastore_name)