from peewee import *
from entities.ent_base_model import BaseModel
from entities.ent_chat_keyword import ChatKeyword
from entities.ent_enabled_module import EnabledModule

""" Auflösungstabelle (N:M) for EnabledModule and ChatKeyword 
by using automatically created id field. """
class EnabledModuleHasChatKeyword(BaseModel):
    enabled_module_id = ForeignKeyField(EnabledModule)
    chat_keyword_id = ForeignKeyField(ChatKeyword) #, to_field="id"