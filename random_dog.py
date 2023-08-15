import requests

def get_dog():
    URL = 'https://random.dog/woof.json'
    r = requests.get(URL)
    data = r.json()
    img_url = data['url']
    return img_url
while True:
    print(get_dog())
