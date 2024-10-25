import requests

url = "http://18.212.37.106/api/dashboard?bot_id=bot_12345"
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
