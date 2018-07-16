import sys
from peewee import *
from entities.ent_enabled_module import EnabledModule

# TODO: Import all modules dynamically
from modules.get_welcome_msg import get_welcome_msg
from modules.get_random_question import get_random_question
from modules.get_random_fact import get_random_fact

def db_loadEnabledModules():
    enabled_modules = []
    for module in EnabledModule.select():
        enabled_modules.append(
            # str to class
            getattr(sys.modules[__name__], module.class_name)
        )
    return enabled_modules