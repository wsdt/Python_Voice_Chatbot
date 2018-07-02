from Answers._Answer import Answer
from chatterbot import ChatBot

chatbot = ChatBot(
    'KevKevin',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

#Train based on english corpus
chatbot.train("chatterbot.corpus.english")


class AnswerQuestion(Answer):
    @staticmethod
    def getAnswer(userInput):
        #return "Sorry, I didn't understand your question."
        return chatbot.get_response(userInput)
