from urllib.parse import urlencode, urlparse
import requests
import json



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

json_string = """ {"count": 216, "items": [30167, 55517, 121096, 178823, 194482, 212002, 235272, 267728, 363210, 404684, 434690, 440358, 564515, 666056, 669616, 672429, 674571, 680992, 693342, 830720, 836357, 854424, 854833, 876823, 941160, 980689, 1000000, 1002988, 1109857, 1127952, 1199578, 1300017, 1303694, 1307683, 1343364, 1379643, 1411905, 1485865, 1562198, 1587185, 1599249, 1693517, 1800058, 1823011, 1865431, 1909241, 1940950, 2074894, 2120730, 2137008, 2159793, 2195357, 2203228, 2206014, 2207048, 2261729, 2282165, 2331534, 2390544, 2419019, 2446111, 2476269, 2591688]} """
parsed_string = json.loads(json_string)

response = requests.get('https://api.vk.com/method/friends.get', params)
print('Исходный ответ', response.json()['response'])
print('Друзья после парсинга', parsed_string["items"])


# получаем список моих друзей онлайн
#response = requests.get('https://api.vk.com/method/friends.getOnline', params)
#print('Мои друзья:', set(response.json()['response']))

my_friens = set(parsed_string["items"])

# получаем список друзей моих друзей
for user_id in parsed_string["items"]:
    response = requests.get('https://api.vk.com/method/friends.get', {'user_id': user_id})
    print('Друзья моих друзей:', set(response.json()['response']))

target_uids = set(response.json()['response'])

# находим пересечение
mutual_friens = my_friens & target_uids

print('Общие друзья', mutual_friens)