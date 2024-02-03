import urllib3
import json

BOT_TOKEN = '6547190050:AAE4Gw9pDYjkmWPc3JrcJp3qIl0t3mCge-Q'

def sendPhoto(chat_id, image_url):
    data = {
        'chat_id': chat_id,
        'photo': image_url,
    }
    http = urllib3.PoolManager()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    response = http.request('POST',url ,fields=data)
    return json.loads(response.data.decode('utf-8'))

result = sendPhoto(6569566686,"https://wikibook.co.kr/images/cover/s/9791158394264.jpg")

print(result)