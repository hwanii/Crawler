from bs4 import BeautifulSoup
import re
from utils import get_top100_list
# source = open('melon.html', 'rt').read()
# soup = BeautifulSoup(source, 'lxml')


# for index, div in enumerate(soup.find_all('div', class_='rank01')):
#     title = div.find('a').text
#     print(index+1, title)
# result = []
# for tr in soup.find_all('tr', class_='lst50'):
#     rank = tr.find('span',class_='rank').text
#     title = tr.find('div',class_='rank01').find('a').text
#     artist = tr.find('div', class_='rank02').find('a').text
#     album = tr.find('div', class_='rank03').find('a').text
#     url_image_cover = tr.find('a',class_='image_typeAll').find('img')['src']
#     p = re.compile(r'(.*\..*?)')
#     url_image_cover = re.search(p, url_image_cover).group(1)
#     result.append({
#         'rank' : rank,
#         'title' : title,
#         'url_img_cover' : url_image_cover,
#         'artist' : artist,
#         'album' : album,
#     })
#
# for item in result:
#     print(item)

if __name__=='__main__':
    result = get_top100_list()
    for item in result:
        print(item)