import requests


def YandexSearch(query):
	    with requests.session() as c:
	        url = 'https://yandex.ru/search/?'
	        query = {'text': user_search_string}
	        urllink = requests.get(url, params=query)
	        print (urllink.url)
	        print (urllink.text)	

# def googleSearch(query):
# 	    with requests.session() as c:
# 	        url = 'https://www.google.com/search?'
# 	        query = {'q': user_search_string}
# 	        urllink = requests.get(url, params=query)
# 	        print (urllink.url)

def Google_Search(payload):                                                                                                                                                                                       
    link = 'http://google.com/'                                                                                                                              
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}                                                                
    payload = {'q': user_search_string}                                                                                                                                                                                     
    response = requests.get(link, headers=ua, params=payload)                                                                                                                                                      
    print (response.text)                                                                                                                                                                                            

	# Google_Search('test')

user_engine_choice = input('Укажите поисковый движок? (yandex <> google): ')
user_search_string = input("Что надо найти? ")

if user_engine_choice == 'yandex':
	user_engine_string = 'https://yandex.ru'
	print("Будем искать в", user_engine_string)
	YandexSearch(user_search_string)
else:
	user_engine_string = 'https://google.com'
	print("Будем искать в", user_engine_string)
	Google_Search(user_search_string)



#resp = requests.get(user_engine_string, data={'text':user_search_string})

# if urllink:
# 	print ('Success')
# else:
# 	print('Error happens')
# 	print(urllink.status_code)

#print(resp.text)