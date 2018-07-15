#!/usr/bin/python3
from answers.get_smart_answer import GetSmartAnswer
from answers.random.get_random_question import AskQuestion
from answers.random.get_random_fact import GetRandomFact
from answers.api.get_instagram_info import GetInstagramAnswer
from answers.get_welcome_msg import GetWelcomeMsg


# Class is responsible for textAnswers.
class PyChatbot():
    # Modules need to implement chat_keywords[]
    # As GetSmartAnswer is only for else-block, there is no need to add it here
    ENABLED_MODULES = [
        GetWelcomeMsg,
        AskQuestion,
        GetRandomFact,
        GetInstagramAnswer
    ]

    # Method also used by TelegramBot
    @staticmethod
    def getAnswer(userInput):
        for module in PyChatbot.ENABLED_MODULES:
            # text should be always a str, bc. we validated this in main.py
            if any(x in str(userInput) for x in module.chat_keywords):
                return module.getAnswer(userInput)

        # Outside of for, so if nothing is returned we get a smart answer, but only if nothing answered until now
        return GetSmartAnswer.getAnswer(userInput)
