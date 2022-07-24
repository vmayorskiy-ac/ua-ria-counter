import requests
import json
import pprint


def complain(article_ids):
    for article_id in article_ids:
        session, msgs = get_messages(article_id)
        comments = msgs['chat_messages']['comment_ids']

        for msg_idx in range(len(comments)):
            if msg_idx % 2 == 0:
                send_complain(session, article_id, comments[msg_idx])

    return comments


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
    return session, res


def send_complain(session, article_id, comment_id):
    #session = requests.Session()
    #session.headers[
    #    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0'
    #session.headers['Origin'] = 'https://ria.ru'
    #session.headers[
    #    'Referer'] = 'https://ria.ru/'
    # print(session.headers)

    service_url = f'https://ria.ru/services/chat/report/'
    data = { 'article_id': f'{article_id}', 'message_id': f'{comment_id}' }
    #data2 = "article_id=1804580090&message_id=62dcc204ddb5d6741c025954"

    response = session.post(url=service_url, json=data)

    print('********************')
    print(response.headers)
    print('********************')
    print(response.status_code)
    print('********************')
    print(response.text)

    #res = json.loads(response.text)
    res = response.text
    return res


def test_complain():
    res = complain(article_ids=[
        '1803240729',
        '1803168150',
        '1803112620',
        '1803307403',
        '1803330519',
        '1803106820',
        '1803108513',
        '1803248526',
        '1803248113',
        '1803185102',
        '1803213451',
        '1803243015',
        '1803257368'])
    #pprint.pprint(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_complain()

