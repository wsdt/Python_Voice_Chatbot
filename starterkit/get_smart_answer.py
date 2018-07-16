from starterkit.abstr_answer import abstr_answer
from starterkit.conf import chatbot

class get_smart_answer(abstr_answer):
    @staticmethod
    def getAnswer(userInput):
        return chatbot.get_response(str(userInput))