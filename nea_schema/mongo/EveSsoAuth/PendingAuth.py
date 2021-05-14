from ming import Session
from ming.odm import ThreadLocalODMSession, MappedClass, FieldProperty
from ming.schema import ObjectId, Binary, DateTime

class PendingAuth(MappedClass):
    class __mongometa__:
        session = ThreadLocalODMSession(doc_session=Session.by_name('EveSsoAuth'))
        name = 'PendingAuth'

    _id = FieldProperty(ObjectId)
    code = FieldProperty(Binary(required=True))
    requested_at = FieldProperty(DateTime(required=True))
