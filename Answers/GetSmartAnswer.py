from Answers._Answer import Answer
import os
import telegram
from chatterbot import ChatBot

# Does bot need to be trained?
trainBot = not os.path.exists('db.sqlite3')

# Creates also sqlite db so validation has to be before!
chatbot = ChatBot(
    'KevKevin',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

#Train based on english corpus IF db does not exist already
if trainBot:
    chatbot.train("chatterbot.corpus.english")


class GetSmartAnswer(Answer):
    @staticmethod
    def getAnswer(bot,update,userInput):
        #return "Sorry, I didn't understand your question."
        update.message.reply_text(str(
            chatbot.get_response(userInput)
        ))
