from peewee import *
from entities.ent_base_model import BaseModel

class ChatKeyword(BaseModel):
    chat_keyword = CharField(unique=True)