from bs4 import BeautifulSoup
import requests
import re
import os
def get_top100_list(refresh_html=False):
    """
    실시간 차트 1~100위의 리스트 반환
    :return:
    """
    url_chart_realtime_50 = 'https://www.melon.com/chart/index.htm'
    url_chart_realtime_100 = 'https://www.melon.com/chart/index.htm#params%5Bidx%5D=51'
    # 프로젝트가 실행되는 '파일'의 path
    # /utils
    path_module = os.path.abspath(__name__)

    # 프로젝트 루트 디렉토리(파일의 path에서 하나 위로 가야지 루트 디렉토리)
    # /
    root_dir = os.path.dirname(path_module)

    # root 디렉토리 안에 data라는 디렉토리 path를 정해줌(아직 만드는 건 아님)
    # /data
    path_data_dir = os.path.join(root_dir, 'data')

    # data란 폴더 가 있을경우 따로 안만들어줌
    # /data 생성
    os.makedirs(path_data_dir, exist_ok=True)

    # 만들 파일의 path 지정(/data/chart_realtime_50.html)
    # /data/chart_realtime_50.html
    file_path_50 = os.path.join(path_data_dir, 'chart_realtime_50.html')

    # 파일을 만들때는 폴더의 path가 아니라 파일의 path를 입력해줘야함
    # 파일이 있는 경우를 검사 후 로직 실행
    if not os.path.exists(file_path_50):
        response = requests.get(url_chart_realtime_50)
        source = response.text
        with open(file_path_50, 'wt') as f:
            f.write(source)
    else:
        print(f'"{file_path_50}" file is already exists!!')


    # try-except문, xt로 파일이 이미 존재하는지 확인
    file_path_100 = os.path.join(path_data_dir, 'chart_realtime_100.html')
    try:
        with open(file_path_100, 'xt') as f:
            response = requests.get(url_chart_realtime_100)
            source = response.text
            f.write(source)
    except FileExistsError as e:
        print(f'"{file_path_100}" file is already exists!!')


    result = []

    # 50위까지

    source = open(file_path_50, 'rt').read()
    soup = BeautifulSoup(source, 'lxml')
    for tr in soup.find_all('tr', class_='lst50'):
        rank = tr.find('span', class_='rank').text
        title = tr.find('div', class_='rank01').find('a').text
        artist = tr.find('div', class_='rank02').find('a').text
        album = tr.find('div', class_='rank03').find('a').text
        url_image_cover = tr.find('a', class_='image_typeAll').find('img')['src']
        p = re.compile(r'(.*\..*?)')
        url_image_cover = re.search(p, url_image_cover).group(1)
        result.append({
            'rank': rank,
            'title': title,
            'url_img_cover': url_image_cover,
            'artist': artist,
            'album': album,
        })

    # 100위까지
    source = open(file_path_100, 'rt').read()
    soup = BeautifulSoup(source, 'lxml')
    for tr in soup.find_all('tr', class_='lst100'):
        rank = tr.find('span', class_='rank').text
        title = tr.find('div', class_='rank01').find('a').text
        artist = tr.find('div', class_='rank02').find('a').text
        album = tr.find('div', class_='rank03').find('a').text
        url_image_cover = tr.find('a', class_='image_typeAll').find('img')['src']
        p = re.compile(r'(.*\..*?)')
        url_image_cover = re.search(p, url_image_cover).group(1)
        result.append({
            'rank': rank,
            'title': title,
            'url_img_cover': url_image_cover,
            'artist': artist,
            'album': album,
        })
    return result