import requests
# Set telegram bot token
from pprint import pprint
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'

def sendPhoto(chat_id:str,photo:str,caption:str):
    """
    This function sends photo to telegram bot
    Args:
        chat_id: chat id
        photo: photo path
        caption: photo caption
    Returns:
        response: response from telegram bot
    """
    URL = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    params = {
        'chat_id':chat_id,
        'photo':photo,
        'caption':caption
    }
    response = requests.get(URL,params=params)
    return response.json()

# Send photo to telegram bot
chat_id = 5575549228
photo ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtET58uAxG_u8uZH2mm-IK0dFNtvhYIxt8HQ&usqp=CAU'
caption = 'This is a cat'
pprint(sendPhoto(chat_id,photo,caption))