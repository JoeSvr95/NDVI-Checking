import mongoengine

from data.pixels import Pixels

class Label(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    extension = mongoengine.StringField(required=True)
    NDVI = mongoengine.FloatField()
    SPAD = mongoengine.FloatField()
    LAB = mongoengine.FloatField()
    pixels = mongoengine.EmbeddedDocumentListField(Pixels)

    meta = {
        'db_alias': 'core',
        'collection': 'labels'
    }