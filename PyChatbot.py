import os
from Answers import GetSmartAnswer
from Answers import AskQuestion
from Answers import GetRandomFact
from Answers import GetInstagramAnswer

# Class is responsible for textAnswers.
class PyChatbot():
    # Modules need to implement chat_keywords[]
    # As GetSmartAnswer is only for else-block, there is no need to add it here
    ENABLED_MODULES = [
        AskQuestion.AskQuestion,
        GetRandomFact.GetRandomFact,
        GetInstagramAnswer.GetInstagramAnswer
    ]

    #Method also used by TelegramBot
    @staticmethod
    def getAnswer(bot, update, userInput):
        if "/start" in userInput:
            update.message.reply_text(str("Welcome to PyChatbot :)"))
        else:
            have_answered = False
            for module in PyChatbot.ENABLED_MODULES:
                if any(x in userInput for x in module.chat_keywords):
                    module.getAnswer(bot,update,userInput)
                    have_answered = True
                    # no break, so we allow for multiple responses

            # Outside of for, so if nothing is returned we get a smart answer, but only if nothing answered until now
            if not have_answered:
                GetSmartAnswer.GetSmartAnswer.getAnswer(bot,update,userInput)

#TODO: add ReplyKeyBoardMarkup with KeyboardButtons etc.