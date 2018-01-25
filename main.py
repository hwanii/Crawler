from utils import get_top100_list, get_song_detail

if __name__=='__main__':
    result = get_top100_list()

    for item in result:
        print(get_song_detail(item['song_id']))
    # print(get_song_detail(30784303))