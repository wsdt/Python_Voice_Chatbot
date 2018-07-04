from Answers._Answer import Answer
import os
import telegram
from chatterbot import ChatBot
from Answers.random.AskRandomQuestion import AskQuestion

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


class GetSmartAnswer(Answer):
    # No chat_keywords, bc. this is the "else"-Answer, if no keywords were found

    @staticmethod
    def getAnswer(bot,update):
        try:
            update.message.reply_text(str(
                chatbot.get_response(update.message.text)
            ))
        except telegram.error.BadRequest as e:
            print("ERROR: Telegram Badrequest -> "+str(e))
            update.message.reply_text("To be honest, I haven't understood this completely. Instead I will ask you sth. :)")
            update.message.reply_text(str(AskQuestion.getAnswer(bot, update)))
