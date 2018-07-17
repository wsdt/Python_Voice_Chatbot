import sys
from peewee import *
from entities.ent_enabled_module import EnabledModule
from entities.ent_chat_keyword import ChatKeyword
from entities.ent_enabled_module_has_chat_keyword import EnabledModuleHasChatKeyword

# TODO: Import all modules dynamically
from modules.get_welcome_msg import get_welcome_msg
from modules.get_random_question import get_random_question
from modules.get_random_fact import get_random_fact


def db_loadEnabledModules():
    enabled_modules = []
    for module in EnabledModule.select():
        enabled_modules.append(
            # str to class
            getattr(sys.modules[__name__], module.class_name)() # make instance out of class
        )
    return enabled_modules


# @param moduleStr: className -> e.g. use: get_welcome_msg().getClassName()
def db_loadChatKeywordsOfModule(moduleStr):
    resultSet = (ChatKeyword.select()
             .where(EnabledModule.class_name == moduleStr)
             .join(EnabledModuleHasChatKeyword)
             .switch(EnabledModuleHasChatKeyword)
             .join(EnabledModule))

    keywords = []
    for keyword_row in resultSet:
        keywords.append(keyword_row.chat_keyword)

    return keywords
