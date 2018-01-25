import re
import requests
__all__ = (
    'get_tag_attribute',
    'get_tag_content',
)

def get_tag_attribute(attribute_name, tag_string):
    # p_first_tag = re.compile(r'^.*?<.*?>',re.DOTALL)
    # first_tag = re.search(p_first_tag,tag_string).group()
    pattern = re.compile(r'^<.*?{}="(?P<value>.*?)".*?>'.format(attribute_name), re.DOTALL)
    m = re.search(pattern, tag_string)
    if m:
        return m.group('value')
    return ''


def get_tag_content(tag_string):
    p = re.compile(r'<.*?>(?P<value>.*)</.*?>', re.DOTALL)
    m = re.search(p, tag_string)
    if m:
        return get_tag_content(m.group('value'))
    elif re.search(r'[<>]',tag_string):
        return ''
    return tag_string

def find_tag(tag, tag_string, class_=None):
    """
    tag_string에서 tag요소를 찾아 리턴
    :param tag:
    :param tag_string:
    :param class_:
    :return:
    """
    p = re.compile(r'.*?(<{tag}.*?{class_}.*?>.*?</{tag}>)'.format(tag = tag,
                                                                   class_ = f'class=".*?{class_}.*?"' if class_ else ''))
    m = re.search(p, tag_string)
    if m:
        return m.group(1)
    return None
def save():
    """
    멜론 사이트의 인기차트 1~50위에 해당하는 페이지를 melon.html로 저장
    :return: None
    """
    r = requests.get('https://www.melon.com/chart/index.htm')
    html = r.text
    f = open('melon.html', 'wt')
    f.write(html)
    f.close()
