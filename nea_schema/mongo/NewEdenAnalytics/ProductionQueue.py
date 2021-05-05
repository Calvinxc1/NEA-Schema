from ming.odm import FieldProperty, MappedClass, ThreadLocalODMSession
from ming.schema import Anything, Object, ObjectId, DateTime
import ming

class ProductionQueue(MappedClass):
    class __mongometa__:
        session = ThreadLocalODMSession(doc_session=ming.Session.by_name('NewEdenAnalytics'))
        name = 'ProductionQueue'

    _id = FieldProperty(ObjectId)
    path = FieldProperty(Object(Anything, required=True))
    selectedStation = FieldProperty(Object(Anything, required=True))
    createdAt = FieldProperty(DateTime(required=True))
