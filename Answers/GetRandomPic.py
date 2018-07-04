from Answers._Answer import Answer
import telegram
from CONFIDENTIAL import AUTHORIZED_USER
from time import strftime, gmtime


class GetRandomPic(Answer):
    chat_keywords = ["pic", "image"]

    @staticmethod
    def getAnswer(bot,update):
        # Send action
        bot.send_chat_action(chat_id=AUTHORIZED_USER, action=telegram.ChatAction.UPLOAD_PHOTO)
        # time attached to avoid caching so each time a new image is sent (so url is unique every time)
        bot.send_photo(chat_id=AUTHORIZED_USER,
                       photo='https://picsum.photos/400?random' + strftime("%Y-%m-%d_%H-%M-%S", gmtime()))

