import telegram
from telegram.ext import Updater, MessageHandler, Filters
import os 

TOKEN = os.environ['TOKEN']

# update = bot.getUpdates()[-1]

# chat_id = update.message.chat.id

# bot.sendMessage(chat_id, "123")
def main(update,context):
    chat_id=update.message.chat.id
    text=update.message.text
    print(text)
    bot=context.bot
    bot.sendMessage(chat_id=chat_id,text=text)
    
    
updater=Updater(TOKEN)
dp=updater.dispatcher

dp.add_handler(MessageHandler(Filters.text, main))

updater.start_polling()
updater.idle()