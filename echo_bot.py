import requests
from pprint import pprint
# Set telegram bot token
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'


# Define a function to get updates from telegram bot
def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url)
    return response.json()

# Define a function to send message to telegram bot
def send_message(chat_id,text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        'chat_id':chat_id,
        'text':text
    }
    response = requests.get(url,params=params)
    return response.json()
while True:
    # Get last message text from updates
    updates = get_updates()
    last_message = updates['result'][-1]['message']['text']
    send_message(5575549228,last_message)