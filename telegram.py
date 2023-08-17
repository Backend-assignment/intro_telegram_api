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