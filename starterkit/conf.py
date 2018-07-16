from chatterbot import ChatBot
from peewee import SqliteDatabase

""" As get_smart_answer is no regular module, the .conf-file here looks completely different. """

# Set database file (MUST NOT BE CHANGED!)
db = SqliteDatabase('db.sqlite3')

# Set up chatbot
chatbot = ChatBot(
    'HOME_ASSISTANT',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)