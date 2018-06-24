import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from PyChatbot import PyChatbot

update_id = None
TOKEN = "440393301:AAHVa5olsKOY66f6NM-lEg1e74pY3jngfCw"

def main():
    global update_id
    bot = telegram.Bot(TOKEN)

    #get first pending update id, this is so we can skip over it in case
    # we get an unauthorized exception
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format=('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    while True:
        try:
            echo(bot)
        except Unauthorized:
            #The user has removed or blocked the bot
            update_id += 1

def echo(bot):
    global update_id
    #Requests updates after the last update id
    for update in bot.get_updates(offset=update_id, timeout=20000):
        update_id = update.update_id +1

        if update.message: #your bot can receive updates without messages
            #reply to msg
            update.message.reply_text(PyChatbot.getAnswer(update.message.text))

if __name__ == '__main__':
    main()

