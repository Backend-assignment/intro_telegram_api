import requests
from pprint import pprint
# Set telegram bot token
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json()
    results = data['result'][-1]
    message = results['message']
  
    photo = message.get('photo')
    if photo:
        photo = photo[-1]
        file_id = photo['file_id']
        print(file_id)
    return response.json()


get_updates()