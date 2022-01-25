import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://animekisa.tv"
URL = "https://animekisa.tv/latest/1"

HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
}

@csrf_exempt
def get_html(url, params = ''):
    req = requests.get(url, headers = HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div', class_='episode-box test')
    anime = []

    for item in items:
        anime.append(
            {
                'title': item.find('div', class_="episode-box-2").get_text(),
                'image': HOST + item.find('div', class_= "image-box").find('img').get('src')

            }
        )
    return anime

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0,1):
            html = get_html(URL, params = {'page': page})
            anime.extend(get_data(html.text))
            return anime
    else:
        raise ValueError('Error in parser function')
