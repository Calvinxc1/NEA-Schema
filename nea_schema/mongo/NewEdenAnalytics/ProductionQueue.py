from ming import Session
from ming.odm import FieldProperty, MappedClass, ThreadLocalODMSession
from ming.schema import Anything, Object, ObjectId, DateTime, Int

class ProductionQueue(MappedClass):
    class __mongometa__:
        session = ThreadLocalODMSession(doc_session=Session.by_name('NewEdenAnalytics'))
        name = 'ProductionQueue'

    _id = FieldProperty(ObjectId)
    priority = FieldProperty(Int(required=True))
    path = FieldProperty(Anything(required=True))
    station = FieldProperty(Anything(required=True))
    created = FieldProperty(DateTime(required=True))
