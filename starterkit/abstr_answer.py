from abc import abstractmethod, ABC
import json
from entities import *

""" PARENT CLASS = MODULE layout 

- How to create a new module?
1. Create a new folder in /modules. Please use the same name for that
folder as for your module-file and the class inside that .py-file.
    e.g.: get_weather_info, get_traffic_info, get_cinema_info, ... 

2. Create a __init__.py in your newly created folder, which imports
both files you will create in your next steps (conf and your module-file). 
Just take a look into __init__.py-files of other modules.

3. Create your module logic by creating a .py-file, which exact the same
name as your superior module folder. 
    e.g. get_welcome_msg.py, get_traffic_info.py, get_cinemy_info.py
    
3.1. Write your logic by extending from this class. As class name, please
use the same name as for your superior directory and the filename of your 
module. Here a small example. 

    class get_weather_info(abstr_answer):
        @staticmethod
        def getAnswer(userInput):
            # Do sth with the userInput, do sth specific or just return
            # a static string. 
            return "Thanks for testing me. You wrote -> "+str(userInput)
            
So, if the userInput contains at least one of your keywords your 
method get's invoked. What you do with the userInput or what you
are answering in general in your method is completely independent
from other modules. 

4. Create a new .py-file named 'conf.py'. This name is obligatory to 
integrate your module successfully into the assistant. This file is 
used to configure your module. You have determined in 3. and 3.1. what
the assistant does/answers, when your method is invoked. But, you haven't
set the keywords yet and other important metadata yet. For that we have 
the conf.py-file. 

    ENABLED_MODULE = EnabledModule( # do not change
        class_name=get_weather_info().getStrClassName(), # just place here the same name as for your superior folder, the class name and the module-file
        custom_json_settings="{}" # Here you could place a json, which can be dynamically used by your module (without restrictions). 
    )
    
    CHAT_KEYWORDS = [ # do not change
        ChatKeyword(chat_keyword="weather"), #create a list of keywords. When one of your keywords is detected your get_answer() get's invoked.
        ChatKeyword(chat_keyword="storm") 
    ]

The 'chat_keywords' is an array, which contains keywords. By placing
several keywords there you can decide when your getAnswer() method 
get's invoked. If your new module causes an error, then at least
one of the keywords you have used is already in use by another enabled
module. So, just remove the other module from the enabled_modules list 
in the setup.py OR change the keyword(s) in your module. 
-> Later, we might add the possibility to use the same keywords as other 
-> modules (for that just leave an issue on Github)
"""

# Extend from ABC (to be abstract) and from EnabledModule (to be a db entity)
class abstr_answer(ABC):
    __chat_keywords = None # private emulation
    __custom_json_settings = None # private emulation

    @abstractmethod
    def getAnswer(self,userInput):
        raise NotImplementedError

    def db_loadCustom_json_settings(self):
        if self.__custom_json_settings is None:
            # Get first row [0], if no row found a exception might be thrown
            self.__custom_json_settings = json.loads((EnabledModule.select().where(EnabledModule.class_name == self.getStrClassName()))[0].custom_json_settings)

        return self.__custom_json_settings

    """ Load chat_keywords from database and return it as list. 
    @param moduleStr: className -> e.g. use: get_welcome_msg().getClassName() """
    def db_loadChatKeywordsOfModule(self):
        resultSet = (ChatKeyword.select()
                     .where(EnabledModule.class_name == self.getStrClassName())
                     .join(EnabledModuleHasChatKeyword)
                     .switch(EnabledModuleHasChatKeyword)
                     .join(EnabledModule))

        #TODO: Maybe return objs in future instead
        keywords = []
        for keyword_row in resultSet:
            keywords.append(str(keyword_row))

        return keywords

    def getChatKeywords(self):
        if self.__chat_keywords is None:
            self.__chat_keywords = self.db_loadChatKeywordsOfModule()
        return self.__chat_keywords

    def getStrClassName(self):
        return str(type(self).__name__)


