from urllib.parse import urlencode, urlparse
import requests


AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.60'
APP_ID = 5900880

auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'response_type': 'token',
    'scope': 'friends,status',
    'v': VERSION,
}
print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))

token_url = 'https://oauth.vk.com/blank.html#access_token=4bcfa16bd2999bac6c6c06165c4acd5fe6584a638a54ba1657a8293d329ca62b0828f50dc45c9907aff2a&expires_in=86400&user_id=1009635'

o = urlparse(token_url)
fragments = dict((i.split('=') for i in o.fragment.split('&')))
access_token = fragments['access_token']

params = {'access_token': access_token,
          'v': VERSION}

response = requests.get('https://api.vk.com/method/friends.getOnline', params)
print(response.json())

for user_id in response.json()['response']:
    response = requests.get('https://api.vk.com/method/friends.get', {'user_id': user_id})
    print(response.json())
