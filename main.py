import os
import sys
import telegram
from telegram.error import NetworkError, Unauthorized
from CONFIDENTIAL import *
from PyChatbot import PyChatbot
from Answers.random import AskRandomQuestion

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
    for update in bot.get_updates(offset=update_id):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # reply to msg
            text = update.message.text
            if text is None:
                # If text is none, then exit
                return errorOccurred(update)  # stop execution, otherwise bot would die

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
    print("User has sent e.g. a sticker.")
    updateObj.message.reply_text("Sorry, but I didn't catch that.")
    return None  # stop execution of superior method


# Determines whether users is whitelisted for chatting
def isAuthorizedUser(chatId):
    return chatId == AUTHORIZED_USER


if __name__ == '__main__':
    main()
