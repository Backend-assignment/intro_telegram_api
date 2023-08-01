import requests
from pprint import pprint
# Set telegram bot token
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'
# Get updates from telegram bot
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# Get telegram bot updates
response = requests.get(url)
# Print response


# Define a function to get text of messages 
def get_messages(response):
    """
    Get text of messages
    
    Args:
        response:
    return:
        messages: list of message
    """
    results = response.json()['result']
    msg = {
        "text":"",
        "username":"",
    }
    messages = []
    for result in results:
        message = result['message']
  
        msg = {
            'text':message['text'],
            'username':message['from']['first_name']
        }
        messages.append(msg)


    return messages

print(get_messages(response))