from chatterbot import ChatBot
from peewee import SqliteDatabase
from global_constants import DB_NAME

""" As get_smart_answer is no regular module, the .conf-file here looks completely different. """

# Set database file
db = SqliteDatabase(DB_NAME)

# Set up chatbot
chatbot = ChatBot(
    'HOME_ASSISTANT',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)