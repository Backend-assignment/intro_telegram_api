import requests
class Bot:
    def __init__(self, token):
        self.token = token
        self.api_url = f'https://api.telegram.org/bot{token}/'

    def get_updates(self):
        method = 'getUpdates'
        url = f'{self.api_url}{method}'
        resp = requests.get(url)
        result_json = resp.json()['result']
        return result_json
    
    def get_me(self):
        method = 'getMe'
        url = f'{self.api_url}{method}'
        resp = requests.get(url)
        result_json = resp.json()['result']
        return result_json
    
    def send_message(self, chat_id, text):
        method = 'sendMessage'
        url = f'{self.api_url}{method}?chat_id={chat_id}&text={text}'
        resp = requests.get(url)
        return resp