import mongoengine

alias_core = 'core'
db = 'labels_db'

def global_init():
    mongoengine.register_connection(alias=alias_core, name=db)