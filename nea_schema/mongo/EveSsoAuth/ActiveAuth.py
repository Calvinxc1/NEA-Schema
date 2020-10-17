from ming import schema
from ming.odm import ThreadLocalODMSession, MappedClass, FieldProperty

class ActiveAuth(MappedClass):
    class __mongometa__:
        session = ThreadLocalODMSession.by_name('EveSsoAuth')
        name = 'ActiveAuth'

    _id = FieldProperty(schema.Int(required=True))
    character_name = FieldProperty(schema.String(required=True))
    access_token = FieldProperty(schema.String(required=True))
    expires_at = FieldProperty(schema.DateTime(required=True))
    refresh_token = FieldProperty(schema.String(required=True))
    scopes = FieldProperty(schema.Array(schema.String, required=True))
    token_type = FieldProperty(schema.String(required=True))
    