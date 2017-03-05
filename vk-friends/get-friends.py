import requests

VERSION = '5.60'
APP_ID = 5900880
common_friend = {'друг': 0}

#https://oauth.vk.com/blank.html#access_token=e87e536a1a6056e2e44cc6f9420273d1da81c98514bb53d443f9a061cdff8ae272dafc18f25c96f956a55&expires_in=86400&user_id=1009635

access_token = 'e87e536a1a6056e2e44cc6f9420273d1da81c98514bb53d443f9a061cdff8ae272dafc18f25c96f956a55' # здесь нужен свой токен
params = {'access_token': access_token, 'v': VERSION}

# все друзья в контакте...
response = requests.get('https://api.vk.com/method/friends.get', params)

# пробую с онлайн друзьями
#response = requests.get('https://api.vk.com/method/friends.getOnline', params)

i = 0
print('Мои друзья:')
for user_id in response.json()['response']['items']:
    i += 1
    get_friend = requests.get('https://api.vk.com/method/users.get', {'user_id': user_id})
    # Получим список всех своих друзей(в контакте):
    print(i, get_friend.json()['response'][0])

    # внесем в словарь друзей
    if user_id in common_friend:
        common_friend[user_id] += 1
    else:
        common_friend[user_id] = 1

i = 0
for user_id in response.json()['response']['items']:
    i += 1
    get_friend_friends = requests.get('https://api.vk.com/method/friends.get',
                                      {'access_token': access_token, 'v': VERSION, 'user_id': user_id})
    # Для каждого своего друга получим список его друзей:
    print(i, 'Друг: ', user_id, '\nДрузья друга: ', get_friend_friends.json())

    # внесем в словарь друзей
    if user_id in common_friend:
        common_friend[user_id] += 1
    else:
        common_friend[user_id] = 1

print('Общие друзья: ')

for key in sorted(common_friend, key=common_friend.get, reverse=True):
    if common_friend[key] > 1:
        print(key, common_friend[key])