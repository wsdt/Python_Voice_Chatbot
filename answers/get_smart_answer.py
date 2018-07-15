from answers.abstr_answer import abstr_answer
import os
from chatterbot import ChatBot

# Does bot need to be trained?
trainBot = not os.path.exists('db.sqlite3')

# Creates also sqlite db so validation has to be before!
chatbot = ChatBot(
    'KevKevin',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

""" Train based on english corpus IF db does not exist already
do this here already, bc. training needs longer than e.g. instagram
login and to avoid answer latencies we just wait a little bit longer
for starting the bot itself. 
"""
if trainBot:
    chatbot.train("chatterbot.corpus.english")


class get_smart_answer(abstr_answer):
    # No chat_keywords, bc. this is the "else"-Answer, if no keywords were found

    @staticmethod
    def getAnswer(userInput):
        return chatbot.get_response(str(userInput))
