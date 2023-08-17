import requests
from telegram import Bot
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'
# Get updates from telegram bot
params = {
    'chat_id':5575549228,
    'text':'Salom'
}
bot = Bot(TOKEN)
bot.send_message(5575549228, 'Salom123')