import re
from regex import utils

source = open('melon.html', 'rt').read()
chart = []
PATTERN_TR = re.compile(r'<tr(.*?)</tr>', re.DOTALL)
tr_list = re.findall(PATTERN_TR, source)


rank = 1
for i in tr_list[1:]:
    PATTERN_TD = re.compile(r'<td.*?></td>', re.DOTALL)
    PATTERN_RANK = re.compile(r'rank ">(.*?)</span>')
    # PATTERN_IMG = re.compile(r'<img.*?src="(.*?)".*?>', re.DOTALL)
    # PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')
    PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
    PATTERN_DIV_RANK02 = re.compile(r'<div class="ellipsis rank02">.*?</div>', re.DOTALL)
    PATTERN_DIV_RANK03 = re.compile(r'<div class="ellipsis rank03">.*?</div>', re.DOTALL)

    td_list = re.findall(PATTERN_TD, i)

    # rank
    # td_title_rank = td_list[1]
    # rank = re.search(PATTERN_RANK, td_title_rank).group(1)

    td_img_cover = td_list[3]
    url_img_cover = utils.get_tag_attribute('src', td_img_cover)

    td_title_author = td_list[5]
    div_rank01 = re.search(PATTERN_DIV_RANK01, td_title_author).group()
    title = utils.get_tag_content(div_rank01)

    td_title_artist = td_list[5]
    div_rank02 = re.search(PATTERN_DIV_RANK02, td_title_artist).group()
    artist = utils.get_tag_content(div_rank02)

    td_title_album = td_list[6]
    div_rank03 = re.search(PATTERN_DIV_RANK03, td_title_album).group()
    album = utils.get_tag_content(div_rank03)

    chart_info = {
        'rank': rank,
        'title': title,
        'artist': artist,
        'album': album,
        'img_url': url_img_cover,
    }
    rank += 1
    chart.append(chart_info)

for i in chart:
    print(i)