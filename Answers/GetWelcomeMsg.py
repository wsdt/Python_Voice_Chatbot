from Answers._Answer import Answer
import telegram
from CONFIDENTIAL import AUTHORIZED_USER
from time import strftime, gmtime


class GetWelcomeMsg(Answer):
    chat_keywords = ["/start"]

    @staticmethod
    def getAnswer(bot,update):
        update.message.reply_text(str("Welcome to PyChatbot :)"))


