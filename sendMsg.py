import requests
from pprint import pprint
# Set telegram bot token
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'
# Get updates from telegram bot
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
params = {
    'chat_id':1478627019,
    'text':'Salom'
}
# Get telegram bot updates
response = requests.get(url,params=params)
# Print response
print(response.status_code)