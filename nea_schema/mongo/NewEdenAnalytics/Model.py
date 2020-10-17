from ming import schema
from ming.odm import ThreadLocalODMSession, MappedClass, FieldProperty

class Model(MappedClass):
    class __mongometa__:
        session = ThreadLocalODMSession.by_name('NewEdenAnalytics')
        name = 'Model'

    _id = FieldProperty(schema.ObjectId)
    model_type = FieldProperty(schema.String(required=True))
    params = FieldProperty(schema.Array(schema.Object({
        'key': schema.String(required=True),
        'val': schema.Anything(required=True),
    }, required=False), required=True))