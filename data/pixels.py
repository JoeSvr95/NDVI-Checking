import mongoengine

class Pixels(mongoengine.EmbeddedDocument):
    label_id = mongoengine.ObjectIdField()
    B = mongoengine.ListField()
    G = mongoengine.ListField()
    R = mongoengine.ListField()