import time
import requests
import urllib.parse
import hmac
import hashlib
import base64

def get_timestamp() -> str:
    return str(round(time.time() * 1000))

def compute_sign(secret: str, timestamp: str) -> str:
    secret_utf8 = secret.encode('utf-8')
    str_to_sign_utf8 = f'{timestamp}\n{secret}'.encode('utf-8')
    hmac_code = hmac.new(secret_utf8, str_to_sign_utf8, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return sign

def send_markdown(secret: str, access_token: str):
    headers = { 'Content-type': 'application/json' }
    url_template = 'https://oapi.dingtalk.com/robot/send?access_token={}&timestamp={}&sign={}'
    def call(title: str, markdown: str):
        timestamp = get_timestamp()
        sign = compute_sign(secret, timestamp)
        url = url_template.format(access_token, timestamp, sign)
        response = requests.post(
            url,
            headers=headers,
            json={
                'msgtype': 'markdown',
                'markdown': {
                    'title': title,
                    'text': markdown
                }
            }
        )
        response_json = response.json()
        if response_json['errcode'] == 0:
            print('ok')
        else:
            print(response_json)
    return call

