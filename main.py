import os
import sys
import telegram
from telegram.error import NetworkError, Unauthorized
from CONFIDENTIAL import *
from PyChatbot import PyChatbot
from Answers.random import AskRandomQuestion
from Answers.api.test_Voice import test_Voice

update_id = None
bot = telegram.Bot(TOKEN)


def main():
    global update_id

    # get first pending update id, this is so we can skip over it in case
    # we get an unauthorized exception
    try:
        update_id = bot.get_updates()[0].update_id
    except (IndexError, telegram.error.TimedOut):
        update_id = None

    while True:
        try:
            echo(bot)
        except Unauthorized:
            # The user has removed or blocked the bot
            update_id += 1


def echo(bot):
    global update_id

    # Avoid timeout exception, which might occur when restarting the bot etc.
    try:
        chat_id = bot.get_updates()[-1].message.chat_id
    except (IndexError, telegram.error.TimedOut):
        return None

    # Requests updates after the last update id
    for update in bot.get_updates(offset=update_id, timeout=10000):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # reply to msg
            text = update.message.text
            if text is None:
                test_Voice.test(update)

                # If text is none, then exit
                return errorOccurred(update)  # stop execution, otherwise bot would die

            """ If you have no idea what your chat_id is, you can look it up here when writing the
            first message to the bot. After you noted down your id, you can copy it into your 
            CONFIDENTIAL.py.
            
            This mechanism protects your IoT-devices and private data from strangers. As I am
            not happy with this validation, I will add here a more secure mechanism in future! """
            print("Users message: '" + text + "' from chat_id -> " + str(update.message.chat.id))
            if isAuthorizedUser(update.message.chat.id):
                try:
                    # Send action
                    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING) #pauschal für alle
                    # answer as text message
                    PyChatbot.getAnswer(bot, update)
                except telegram.error.TimedOut as e:
                    print("ERROR: Telegram timeOutException: "+str(e))
            else:
                update.message.reply_text("FORBIDDEN: Sorry, but I am not allowed to talk with you :).")


def errorOccurred(updateObj):
    print("User has sent a unsupported message/media (e.g. sticker).")
    updateObj.message.reply_text("Sorry, but I didn't catch that.")
    return None  # stop execution of superior method


# Determines whether users is whitelisted for chatting
def isAuthorizedUser(chatId):
    return chatId == AUTHORIZED_USER


if __name__ == '__main__':
    main()
