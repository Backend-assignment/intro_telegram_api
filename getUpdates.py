import requests
from pprint import pprint
# Set telegram bot token
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'
# Get updates from telegram bot
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# Get telegram bot updates
response = requests.get(url)
# Print response
pprint(response.json())
# Define a function to get text of messages 
def get_messages(response):
    """
    Get text of messages
    
    Args:
        response:
    return:
        messages: list of message
    """
    msg = {
        "text":"",
        "username":"",
    }
    messages = []

    return messages