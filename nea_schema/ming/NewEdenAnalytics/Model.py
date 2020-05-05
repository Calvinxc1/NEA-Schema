from ming import schema
from ming.odm import ThreadLocalODMSession, MappedClass, FieldProperty

class Model(MappedClass):
    class __mongometa__:
        session = ThreadLocalODMSession.by_name('NewEdenAnalytics')
        name = 'Models'

    _id = FieldProperty(schema.ObjectId)
    model_name = FieldProperty(schema.String(required=True))
    params = FieldProperty(schema.Array(schema.Object({
        'name': schema.String(required=True),
        'value': schema.Anything(required=True),
    }), required=False))