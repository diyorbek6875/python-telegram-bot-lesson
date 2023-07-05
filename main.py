import telegram
import os 

TOKEN = os.environ['TOKEN']

bot = telegram.Bot(TOKEN)

update = bot.getUpdates()[-1]

chat_id = update.message.chat.id

bot.sendMessage(chat_id, "123")