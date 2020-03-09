import requests

r = requests.get('https://yandex.ru', data={'search':'pypi'})
print(r.text)