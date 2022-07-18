import requests
import json
import pprint


def get_comment_urls(article_id, comment_quotes=[]):
    #url = 'https://ria.ru/20220716/1802988486.html?chat_message_id=62d3219b61fa008202ccd037&chat_room_id=1802988486'
    #comment_quotes = ['В троллейбусное депо', 'наступает ночь,']


    res_urls = []
    res_likes = []
    res_good_like_counts = []

    msgs = get_messages(article_id)

    for quote in comment_quotes:
        msg_url = ''
        msg_like = 's1:1'
        msg_good_like_count = 0
        for msg in msgs['chat_messages']['messages']:
            if msg['text'].startswith(quote):
                # match
                msg_found = True
                msg_id = msg['id']
                txt = msg['text']
                print(f'{msg_id}: {txt}')

                msg_url = f'https://ria.ru/20220716/{article_id}.html?chat_message_id={msg_id}&chat_room_id={article_id}'

                # get emoji
                for emoji in msgs['emoji_chat']:
                    s1 = 1
                    if msg_id == emoji['object_id']:
                        s1 = emoji['emotions']['s1']
                        s2 = emoji['emotions']['s2']
                        s3 = emoji['emotions']['s3']
                        msg_like = f's1:{s1}'
                        msg_good_like_count = s1 + s2 + s3

                        if s2 > 0:
                            msg_like = msg_like + f', s2:{s2}'

        res_urls.append(msg_url)
        res_likes.append(msg_like)
        res_good_like_counts.append(msg_good_like_count)


    return res_urls, res_likes, res_good_like_counts


def get_messages(article_id):
    session = requests.Session()
    session.headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0'
    session.headers['Origin'] = 'https://ria.ru'
    session.headers[
        'Referer'] = 'https://ria.ru/'
    #print(session.headers)

    service_url = f'https://ria.ru/services/chat/get_unread_message/?article_id={article_id}&limit=1000'

    response = session.get(service_url)

    print('********************')
    print(response.headers)
    print('********************')
    print(response.status_code)
    print('********************')
    #print(response.text)

    res = json.loads(response.text)
    return res


def test_get_comment_urls():
    comment_quotes = [
        "Срочно выражайте озабоченность! Если ничего не можете с этим поделать,то не пишите",
        "А где наше хваленое противоспутниковое оружие?",
        "Где удар по центру принятия решений???",
        "Лазерные пушки, и джидайские мечи)))"
    ]

    res = get_comment_urls(article_id='1801858016', comment_quotes=comment_quotes)
    #res = get_comment_urls(article_id='1803079781')
    pprint.pprint(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_get_comment_urls()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
