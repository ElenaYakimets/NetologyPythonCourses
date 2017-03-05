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

token_url = 'https://oauth.vk.com/blank.html#access_token=e87e536a1a6056e2e44cc6f9420273d1da81c98514bb53d443f9a061cdff8ae272dafc18f25c96f956a55&expires_in=86400&user_id=1009635'

o = urlparse(token_url)
fragments = dict((i.split('=') for i in o.fragment.split('&')))
access_token = fragments['access_token']

params = {'access_token': access_token,
          'v': VERSION}

response = requests.get('https://api.vk.com/method/friends.getOnline', params)
print('Мои друзья:', (response.json()['response']))



for user_id in response.json()['response']:
    response = requests.get('https://api.vk.com/method/friends.get', {'user_id': user_id})
    print('Друзья моих друзей:', list(response.json()['response']))

target_uids = list(response.json()['response'])

params2 = {'access_token': access_token,
    'target_uids': target_uids}

print('Количество друзей моих друзей:', len(target_uids))

# response2 = requests.get('https://api.vk.com/method/friends.getMutual', params2)
# print('Общие друзья с', response2.json())