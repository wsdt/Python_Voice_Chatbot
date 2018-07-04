from Answers.GetSmartAnswer import GetSmartAnswer
from Answers.random.AskRandomQuestion import AskQuestion
from Answers.random.GetRandomFact import GetRandomFact
from Answers.api.GetInstagramAnswer import GetInstagramAnswer
from Answers.GetWelcomeMsg import GetWelcomeMsg
from Answers.random.GetRandomPic import GetRandomPic


# Class is responsible for textAnswers.
class PyChatbot():
    # Modules need to implement chat_keywords[]
    # As GetSmartAnswer is only for else-block, there is no need to add it here
    ENABLED_MODULES = [
        GetWelcomeMsg,
        AskQuestion,
        GetRandomFact,
        GetRandomPic,
        GetInstagramAnswer
    ]

    # Method also used by TelegramBot
    @staticmethod
    def getAnswer(bot, update):
        have_answered = False
        for module in PyChatbot.ENABLED_MODULES:
            # text should be always a str, bc. we validated this in main.py
            if any(x in update.message.text for x in module.chat_keywords):
                module.getAnswer(bot, update)
                have_answered = True
                # no break, so we allow for multiple responses

        # Outside of for, so if nothing is returned we get a smart answer, but only if nothing answered until now
        if not have_answered:
            GetSmartAnswer.getAnswer(bot, update)
