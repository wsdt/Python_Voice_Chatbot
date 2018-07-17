from starterkit.abstr_answer import abstr_answer
from starterkit.fallback_module.conf import chatbot

class get_smart_answer(abstr_answer):
    def getAnswer(self,userInput):
        return chatbot.get_response(str(userInput))