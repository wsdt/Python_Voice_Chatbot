from peewee import *
from starterkit.conf import db

def db_loadEnabledModules():
    # TODO: online (https://sqliteonline.com/) all sql tables are created, but here it seems that only the chatterbot ones are created
    print(str(
        db.get_tables()
    ))

db_loadEnabledModules()