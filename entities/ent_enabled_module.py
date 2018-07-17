from peewee import *
from entities.ent_base_model import BaseModel

# IMPORTANT: Peewee automatically creates an id (integer) field as primary key
class EnabledModule(BaseModel):
    class_name = CharField(unique=True)
    custom_json_settings = TextField()