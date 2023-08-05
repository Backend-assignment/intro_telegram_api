import requests
from pprint import pprint
# Set telegram bot token
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'


def sendPhoto(chat_id:str,photo:str,caption:str=''):
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

def get_file_id():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json()
    results = data['result'][-1]
    message = results['message']
    file_id = ''
    photo = message.get('photo')
    if photo:
        photo = photo[-1]
        file_id = photo['file_id']
        
    return file_id
chat_id = 5575549228
file_id = get_file_id()

sendPhoto(chat_id,file_id)