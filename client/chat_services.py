import requests
import json
import pprint
import random
import time


def get_top_chat_rooms():
    article_ids = []

    list = get_rooms()
    toks_1 = list.split("<a class=\"r-list__item\" data-id=\"")

    for tok in toks_1:
        if tok.strip():
            article_id = tok.split('"')[0]
            article_ids.append(article_id)

    return article_ids


def get_rooms():
    session = requests.Session()
    session.headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0'
    session.headers['Origin'] = 'https://ria.ru'
    session.headers[
        'Referer'] = 'https://ria.ru/'
    #print(session.headers)

    service_url = f'https://ria.ru/services/chat/get_rooms/'

    response = session.get(service_url)

    print('********************')
    print(response.headers)
    print('********************')
    print(response.status_code)
    print('********************')
    #print(response.text)

    res = response.text
    return res


def test_get_rooms():
    res = get_top_chat_rooms()
    pprint.pprint(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #main()
    test_get_rooms()

