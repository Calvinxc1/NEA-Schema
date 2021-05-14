from ming import Session
from ming.odm import ThreadLocalODMSession, MappedClass, FieldProperty
from ming.schema import Int, String, DateTime, Array

class ActiveAuth(MappedClass):
    class __mongometa__:
        session = ThreadLocalODMSession(doc_session=Session.by_name('EveSsoAuth'))
        name = 'ActiveAuth'

    _id = FieldProperty(Int(required=True))
    character_name = FieldProperty(String(required=True))
    access_token = FieldProperty(String(required=True))
    expires_at = FieldProperty(DateTime(required=True))
    refresh_token = FieldProperty(String(required=True))
    scopes = FieldProperty(Array(String, required=True))
    token_type = FieldProperty(String(required=True))
    