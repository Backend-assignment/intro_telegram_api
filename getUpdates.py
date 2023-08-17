import requests
from telegram import Bot
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'
# Get updates from telegram bot
bot = Bot(TOKEN)
updates = bot.get_updates()

print(updates)