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
photo ='AgACAgIAAxkBAANRZM3ml30iuntEkUC_AvC1orK_Ap8AAg_SMRvF42lKnGunPrz-3AoBAAMCAANzAAMvBA'
caption = 'This is a cat'
pprint(sendPhoto(chat_id,photo,caption))