import requests
from bs4 import BeautifulSoup

'''
    САМОЕ ВАЖНОЕ - ИМЕНА ПЕРЕМЕННЫХ И ФУНКЦИЙ
    Так
    Кто такой URL1? 
    URLS = {
        'vk':...
        ...
    }
    Не?
    и не url_of_acc
    в этой переменной главное что это урл пользователя. 
    То что главнее, то первее (account_url!!!)

    ДАЛЕЕ
    А что если что-то не так пошло в функции, где try/catch?

    Почему контент то, заменить на более конкретное (get_content_from_vk...)

    Вся прога очень похожа на класс, но без класса)))))
    так ты бы обошелся без глобальных переменных, их лучше вообще не трогать
'''

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Accept": "*/*",
}

def get_content_from_vk(html):
    soup = BeautifulSoup(html, "html.parser")
    person = {
        'name': '-',
        'on/of': '-',
        'status': '-',
        'Profile Info': '-'
    }

    is_group = soup.find("div", class_="line_value")
    if is_group != None:
        person["status"] = "It is a group"
        return person        

    is_close_group = soup.find("div", class_="module clear page_list_module _module")
    if is_close_group != None:
        person["status"] = "It is a close group"
        return person
    
    was_baned = soup.find("img", class_="blocked_image")
    if was_baned != None:
        person["name"] = soup.title.text
        person["status"] = "This page was baned"
        return person

    person["name"] = soup.find("h1", class_="page_name").get_text()
    close_profile = soup.find("div", class_="profile_closed_wall_dummy_title")
    if close_profile != None:
        person["on/of"] = soup.find("div", class_="profile_online_lv").get_text()
        person["status"] = "close profile"
        person["Profile info"] = soup.find("div", class_="profile_info profile_info_short").get_text(separator=" ", strip=True)
        return person

    hidden_page = soup.find("h5", class_="profile_deleted_text")
    if hidden_page != None:
        person["status"] = "hidden page"
        return person
    else:
        person["on/of"] = soup.find("div", class_="profile_online_lv").get_text()
        person["status"] = "open profile"
        person["Basic info"] = soup.find("div", class_="profile_info profile_info_short").get_text(strip=True, separator=" ")
        return person

def get_content_from_twitter(html):
    soup = BeautifulSoup(html, "html.parser")
    person = {
        'name': soup.find_all("div", class_="css-1dbjc4n"),
        'status': '-',
        'Profile Info': '-'
    }

    close_profile = soup.find("svg", class_="r-hkyrab r-4qtqp9 r-yyyyoo r-1xvli5t r-9cviqr r-dnmrzs r-bnwqim r-1plcrui r-lrvibr")
    if close_profile != None:
        person["status"] = "close profile"
        return person

    person["Profile Info"] = soup.find("div", class_="css-1dbjc4n r-1adg3ll r-15d164r")
    authentic_profile = soup.find("svg",class_="r-13gxpu9 r-4qtqp9 r-yyyyoo r-1xvli5t r-9cviqr r-dnmrzs r-bnwqim r-1plcrui r-lrvibr")
    if authentic_profile != None:
        person["status"] = "authentic profile"
        return person
    else:
        person["status"] = "open profile"
        return person

def get_content_from_facebook(html):
    soup = BeautifulSoup(html, "html.parser")

def get_content_from_tiktok(html):
    soup = BeautifulSoup(html, "html.parser")

def get_content_from_badoo(html):
    soup = BeautifulSoup(html, "html.parser")

def get_content_from_ask(html):
    soup = BeautifulSoup(html, "html.parser")

def get_content_from_myspace(html):
    soup = BeautifulSoup(html, "html.parser")

def parse(html, url):    
    if html.status_code == 200:
        if url.find('vk') != -1:
            result = get_content_from_vk(html.text)
        elif url.find('twitter') != -1:
            result = get_content_from_twitter(html.text)
        '''elif url.find('facebook') != -1:
            result = get_content_from_facebook(html.text)
        elif url.find('tiktok') != -1:
            result = get_content_from_tiktok(html.text)
        elif url.find('badoo') != -1:
            result = get_content_from_badoo(html.text)
        elif url.find('ask') != -1:
            result = get_content_from_ask(html.text)
        else:
            result = get_content_from_myspace(html.text)'''
        return result
    elif html.status_code == 404:
        print("{} does not exist".format(url))
        result = None
    else:
        print("Sorry, but we can not parse any information about {} right now".format(url))
        result = None

if __name__ == '__main__':
    username = input()
    URLS = ("https://vk.com",
        "https://twitter.com",
        "https://www.facebook.com",
        "https://www.tiktok.com",
        "https://badoo.com",
        "https://ask.fm",
        "https://myspace.com"
    )
    for URL in URLS:
        if URL == "https://www.tiktok.com":
            sign_to_add = '/@'
        else:
            sign_to_add = '/'
        url = sign_to_add.join([URL, username])
        html = requests.get(url, headers=HEADERS, params=None)
        result = parse(html, url)
        if result != None:
            print (result)