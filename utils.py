from bs4 import BeautifulSoup
import requests
import re
import os
def get_top100_list(refresh_html=False):
    """
    실시간 차트 1~100위의 리스트 반환
    :return:
    """
    url_chart_realtime = 'https://www.melon.com/chart/index.htm'
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
    file_path = os.path.join(path_data_dir, 'chart_realtime.html')

    # 파일을 만들때는 폴더의 path가 아니라 파일의 path를 입력해줘야함
    # 파일이 있는 경우를 검사 후 로직 실행
    # refresh_html 매개변수가 true일 경우, 무조건 새로 파일을 다운받도록 함 -> 존재하지 않을때 덮어써 또는 매개변수 true일때
    if not os.path.exists(file_path) or refresh_html:
        response = requests.get(url_chart_realtime)
        source = response.text
        with open(file_path, 'wt') as f:
            f.write(source)
    else:
        print(f'"{file_path}" file is already exists!!')


    # # try-except문, xt로 파일이 이미 존재하는지 확인
    # file_path = os.path.join(path_data_dir, 'chart_realtime.html')
    # try:
    #     word = 'wt' if refresh_html else 'xt'
    #     with open(file_path, word) as f:
    #         response = requests.get(url_chart_realtime)
    #         source = response.text
    #         f.write(source)
    # except FileExistsError as e:
    #     print(f'"{file_path}" file is already exists!!')

    result = []

    source = open(file_path, 'rt').read()
    soup = BeautifulSoup(source, 'lxml')
    for tr in soup.find_all('tr', class_=['lst50','lst100']): # 멀티 class 지정
        rank = tr.find('span', class_='rank').text
        title = tr.find('div', class_='rank01').find('a').text
        artist = tr.find('div', class_='rank02').find('a').text
        album = tr.find('div', class_='rank03').find('a').text
        url_image_cover = tr.find('a', class_='image_typeAll').find('img').get('src')
        p = re.compile(r'(.*\..*?)/')
        url_image_cover = re.search(p, url_image_cover).group(1)
        data_song_no = tr.get('data-song-no')
        result.append({
            'rank': rank,
            'title': title,
            'url_img_cover': url_image_cover,
            'artist': artist,
            'album': album,
            'song_id' : data_song_no,
        })

    return result


def get_song_detail(song_id, refresh_html = False):
    """
    song_id에 해당하는 곡 정보 dict를 반환

    :param song_id:
    :return:
    """

    path_data = os.path.join(os.getcwd(), 'data', f'{song_id}.html')
    if not os.path.exists(path_data) or refresh_html:
        response = requests.get(f'https://www.melon.com/song/detail.htm?songId={song_id}')
        source = response.text
        with open(path_data, 'wt') as f:
            f.write(source)
    else:
        print(f'"{path_data}" file is already exists!!')

    source = open(path_data, 'rt').read()
    soup = BeautifulSoup(source, 'lxml')
    title_raw = soup.find('div', class_='song_name').contents[2]
    title = re.sub('\\t|\\n','',title_raw)
    artist = soup.find('div', class_='artist').find('span').text
    album = soup.find('dl', class_='list').find('a').text
    publish_date = soup.find('dl', class_='list').contents[7].text
    genre = soup.find('dl', class_='list').contents[11].text
    lyric_raw = soup.find('div', class_='lyric').text
    lyric = re.sub('\\t|\\n', '', lyric_raw)
    song_dic = {
        'title' : title,
        'artist' : artist,
        'album' : album,
        'published_date' : publish_date,
        'genre' : genre,
        'lyric' : lyric,
    }
    return song_dic

# 숙제 : song_id 추가, get_song_detail 함수 완성, song_detail_{song_id}.html 파일 생성되게