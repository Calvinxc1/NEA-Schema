from ming import schema
from ming.odm import ThreadLocalODMSession, MappedClass, FieldProperty

class PendingAuth(MappedClass):
    class __mongometa__:
        session = ThreadLocalODMSession.by_name('EveSsoAuth')
        name = 'PendingAuth'

    _id = FieldProperty(schema.ObjectId)
    code = FieldProperty(schema.Binary(required=True))
    requested_at = FieldProperty(schema.DateTime(required=True))