import urllib3
import json

BOT_TOKEN = '6547190050:AAE4Gw9pDYjkmWPc3JrcJp3qIl0t3mCge-Q'

def get_updates():
    http = urllib3.PoolManager()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = http.request('GET', url)
    return json.loads(response.data.decode('utf-8'))

# Get the latest updates
updates = get_updates()

print(updates)