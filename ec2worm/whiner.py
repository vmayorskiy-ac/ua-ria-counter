import requests
import json
import pprint
import random
import time
import params
import ec2


def main():
    try:
        article_ids, ec2_end_action, apply_ec2_end_action = params.get_params_for_whiner()
        #pprint.pprint(article_ids)

        article_id = random.choice(article_ids)
        complain(article_id)

    except:
        print('Exception occured')

    ec2.terminate_self(action=ec2_end_action, apply_action=apply_ec2_end_action)


def complain(article_id, loops=10):
    session, msgs = get_messages(article_id)
    comments = msgs['chat_messages']['comment_ids']

    for loop in range(loops):
        comment_id = random.choice(comments)
        send_complain(session, article_id, comment_id)
        time.sleep(2)

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
    pprint.pprint(data)

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
    main()
    #test_complain()

