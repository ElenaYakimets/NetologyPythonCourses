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

# получаем список моих друзей
response = requests.get('https://api.vk.com/method/friends.getOnline', params)
print('Мои друзья:', set(response.json()['response']))

my_friens = set(response.json()['response'])

# получаем список друзей моих друзей
for user_id in response.json()['response']:
    response = requests.get('https://api.vk.com/method/friends.get', {'user_id': user_id})
    print('Друзья моих друзей:', set(response.json()['response']))

target_uids = set(response.json()['response'])

# находим пересечение
mutual_friens = my_friens & target_uids

print('Общие друзья', mutual_friens)