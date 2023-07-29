import requests
# Set telegram bot token
TOKEN ='5913199109:AAFUlVr6ZUsPu4nUXXaBSFp6gQSOaZF9mGY'
# URL for get telegram bot info
url = f"https://api.telegram.org/bot{TOKEN}/getMe"

# Get telegram bot info
response = requests.get(url)
# Print response
print(response.json())