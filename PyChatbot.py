import os
from Answers import AnswerQuestion
from Answers import AskQuestion
from Answers import GetRandomFact

# Class is responsible for textAnswers.
class PyChatbot():
    #Method also used by TelegramBot
    @staticmethod
    def getAnswer(userInput):
        if "/start" in userInput:
            return "Welcome to PyChatbot :)"
        elif any(x in userInput for x in ["fact","entertain","quote"]):
            return GetRandomFact.GetRandomFact.getAnswer(userInput)
        elif any(x in userInput for x in ["ask","question"]):
            return AskQuestion.AskQuestion.getAnswer(userInput)
        else:
            return AnswerQuestion.AnswerQuestion.getAnswer(userInput)