from Answers.GetSmartAnswer import GetSmartAnswer
from Answers.random.AskRandomQuestion import AskQuestion
from Answers.random.GetRandomFact import GetRandomFact
from Answers.api.GetInstagramAnswer import GetInstagramAnswer
from Answers.GetWelcomeMsg import GetWelcomeMsg


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
