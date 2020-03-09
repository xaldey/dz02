import requests

def YandexSearch(query):
	    with requests.session() as c:
	        url = 'https://yandex.ru/search/?'
	        query = {'text': user_search_string}
	        urllink = requests.get(url, params=query)
	        print (urllink.url)
	        print (urllink.text)	

def googleSearch(query):
	    with requests.session() as c:
	        url = 'https://www.google.com/search?'
	        query = {'q': user_search_string}
	        urllink = requests.get(url, params=query)
	        print (urllink.url)


user_engine_choice = input('Укажите поисковый движок? (yandex <> google): ')
print(user_engine_choice)

if user_engine_choice == 'yandex':
	user_engine_string = 'https://yandex.ru'
	print("Будем искать в", user_engine_string)
	user_search_string = input("Что надо найти? ")
	YandexSearch(user_search_string)
else:
	user_engine_string = 'https://google.com'
	print("Будем искать в", user_engine_string)
	user_search_string = input("Что надо найти? ")
	googleSearch(user_search_string)

#resp = requests.get(user_engine_string, data={'text':user_search_string})

# if urllink:
# 	print ('Success')
# else:
# 	print('Error happens')
# 	print(urllink.status_code)

#print(resp.text)