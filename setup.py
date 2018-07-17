import os
from global_constants import DB_NAME

# We have to determine this BEFORE calling other imports to prevent creating an empty db before execution of config-script
db_exists =  os.path.exists(DB_NAME)

from peewee import *
import modules
from starterkit.fallback_module.conf import chatbot, db
from entities.ent_chat_keyword import ChatKeyword
from entities.ent_enabled_module import EnabledModule
from entities.ent_enabled_module_has_chat_keyword import EnabledModuleHasChatKeyword

""" This file is only needed ONCE (when executing the assistant the first time).

 If you want to reset your assistant just delete the 'db.sqlite3' in the project's
 root directory and restart this script. """


""" ++++++++++++++++++++++ Assistant modules +++++++++++++++++++++++++++++++++++++++ 
No modules are required. If you don't want to use any additional features, then
you can change the following array to an empty one: 
    ENABLED_MODULES = []
    
If you disabled all modules then the assistant can only talk with you (= get_smart_answer). 
By this you can also easily add some modules to your project and place it here into the list. 
The more modules you have enabled the longer a potential answer of the bot might need. 

You can also create modules by your own. Just look into abstr_answer.py for a more detailed
documentation. When you created one you place your module files into the 'modules' package 
to keep the project structure clean and then just import it here and place it in the 
'ENABLED_MODULES'-array. 

CHANGE:     ++ OPTIONAL ++ [-> by default, the assistant uses all modules] """

""" Your IDE might indicate that no reference has been found in __init__.py. 
     As we are importing all modules dynamically, you can safely ignore this warning. """
ENABLED_MODULES = [
    modules.get_welcome_msg,
    modules.get_random_question,
    modules.get_random_fact
] # DO NOT add get_smart_answer.py here, bc. it is not a module



""" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++ BELOW CODE SHOULDN'T BE CHANGED, UNLESS YOU KNOW WHAT YOU ARE DOING +++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """

if not db_exists: # do not evaluate here again whether db exists (bc. of imports and automatic creation on connection etc.)
    print("Starting assistant setup.")

    """ +++++++++ Train assistant (= default module (not removeable without coding) +++
    -> Train bot/assistant with default language (english) """
    print("Training assistant, this can take a while.")
    chatbot.train("chatterbot.corpus.english")


    # +++++++++++++++++++++++ Database setup - Persistence ++++++++++++++++++++++++++
    print("CONFIDENTIAL: Starting db setup.")

    # Connect to db, create db structure and insert data
    db.connect()
    db.create_tables([
        EnabledModule, ChatKeyword, EnabledModuleHasChatKeyword
    ])

    # INSERT all configured/enabled modules ++++++++++++++++++++++
    for module in ENABLED_MODULES:
        # Save configured module from conf.py file
        if module.conf.ENABLED_MODULE.save() <= 0:
            print("CONFIDENTIAL:ERROR: Could not enable module -> "+str(module.conf.ENABLED_MODULE.class_name))
        # Save all keywords of enabled module + save relationship afterwards
        for chat_keyword in module.conf.CHAT_KEYWORDS:
            # Save keyword
            if chat_keyword.save() <= 0:
                print("CONFIDENTIAL:ERROR: Could not save keyword -> "+str(chat_keyword.chat_keyword))
            # Create relationship to module
            if EnabledModuleHasChatKeyword(
                enabled_module_id=module.conf.ENABLED_MODULE,
                chat_keyword_id=chat_keyword
            ).save() <= 0:
                print("CONFIDENTIAL:ERROR: Could not establish relationship between -> "+str(module.conf.ENABLED_MODULE.class_name)+" and "+str(chat_keyword.chat_keyword))


    print("CONFIDENTIAL: Ended db setup.")


    # TODO: Delete conf.py's after successful installation (or ask user to remove installation data = BETTER), bc. only needed once



else:
    print("CONFIDENTIAL: Found database 'db.sqlite3'. Stopping script execution.\n"+
          "Solution -> Delete the database file and re-execute this script OR just start the main.py.")
