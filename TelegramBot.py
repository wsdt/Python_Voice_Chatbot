import os
import sys
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep, strftime, gmtime
from CONFIDENTIAL import *
from PyChatbot import PyChatbot

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
    for update in bot.get_updates(offset=update_id, timeout=20000):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # reply to msg
            text = update.message.text
            print("Users message: '"+text+"' from chat_id -> "+str(update.message.chat.id))
            if isAuthorizedUser(update.message.chat.id):
                if any(x in text for x in ["pic", "image"]):
                    # Send action
                    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
                    sleep(3)
                    # time attached to avoid caching so each time a new image is sent (so url is unique every time)
                    bot.send_photo(chat_id=chat_id,
                                   photo='https://picsum.photos/400?random' + strftime("%Y-%m-%d_%H-%M-%S", gmtime()))
                else:
                    # Send action
                    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                    sleep(2)
                    # answer as text message
                    textAnswer = PyChatbot.getAnswer(text)
                    try:
                        #TODO: Why do we get a statementObj sometimes?
                        update.message.reply_text(str(textAnswer))
                    except (telegram.error.BadRequest, TypeError):
                        update.message.reply_text("An internal error occurred :(")
            else:
                update.message.reply_text("FORBIDDEN: Sorry, but I am not allowed to talk with you :).")

# Determines whether users is whitelisted for chatting
def isAuthorizedUser(chatId):
    isAuthorized = False
    for authorizedChatId in AUTHORIZED_USERS:
        if chatId == authorizedChatId:
            isAuthorized = True

    return isAuthorized


if __name__ == '__main__':
    main()
