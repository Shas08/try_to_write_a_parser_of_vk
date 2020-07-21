import requests
from bs4 import BeautifulSoup

URL = 'https://vk.com/' + input()
HEADERS = {'User-Agent': 'your or other user-agent', 'Accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    is_group = soup.find('div', class_='line_value')
    was_baned = soup.find('img', class_='blocked_image')
    if is_group != None:
        print('It is group')
        exit(0)
    is_group = soup.find('div', class_='module clear page_list_module _module')
    if is_group != None:
        print('It is a close group')
        exit(0)
    if was_baned != None:
        print(soup.title.text)
        print('This page was baned')
        exit(0)
    close_profile = soup.find('div', class_='profile_closed_wall_dummy_title')
    hidden_page = soup.find('h5', class_='profile_deleted_text')
    if close_profile != None:
        person = {'name': soup.find('h1', class_='page_name').get_text(), 'on/of': soup.find('div', class_='profile_online_lv').get_text(),
        'status': soup.find('div', class_='page_current_info').get_text(), 'Profile info': soup.find('div', class_='profile_info profile_info_short').get_text(separator=' ', strip=True)}
    else: 
        if hidden_page != None:
            person = {
                'name': soup.find('h1', class_='page_name').get_text(), 'status': hidden_page.get_text()}
        else:
            person = {
                'name': soup.find('h1', class_='page_name').get_text(), 'on/of': soup.find('div', class_='profile_online_lv').get_text(), 'Basic info': soup.find('div', class_='profile_info profile_info_short').get_text(strip=True, separator=' ')
            }
    '''
    status = soup.find('span', class_='current_text')
    if status == None:
        person = {'name': soup.find('h1', class_='page_name').get_text(),
        'status': soup.find('div', class_='page_current_info').get_text()}
    else:
        person = {'name': soup.find('h1', class_='page_name').get_text(),
        'status': status.get_text()}
    #items = soup.find('h1', class_='page_name').get_text()
    '''
    print(person)
    

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('This account does not exist')

parse()