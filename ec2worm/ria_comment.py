import random
import boto3
import requests
import pprint
import time
from urllib import parse
import threading

import params
import ec2


def main():
    urls, like_distro, loops_distro, ec2_end_action, apply_ec2_end_action = params.get_params_for_comment()

    threads = []
    for instance_num in range(len(urls)):
        url = urls[instance_num]

        if url.strip():
            loops = loops_distro[instance_num]
            #print(f'instance_num: {instance_num}, loops: {loops_distro}, like_distro: {like_distro}')
            article_id = parse.parse_qs(parse.urlparse(url).query)['chat_room_id'][0]
            comment_id = parse.parse_qs(parse.urlparse(url).query)['chat_message_id'][0]

            thr = threading.Thread(target=run_for_url, args=(url, loops, like_distro[instance_num], article_id, comment_id))
            threads.append(thr)
            thr.start()

            #run_for_url(url, loops, like_distro[instance_num], article_id, comment_id)

    for t in threads:
        t.join()

####    ec2.terminate_self(action=ec2_end_action, apply_action=apply_ec2_end_action)


def run_for_url(url, loops, likes, article_id, comment_id):
    for i in range(loops):
        time.sleep(0.25)
        response = requests.get(url)

        session = requests.Session()
        session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0'
        session.headers['Origin'] = 'https://ria.ru'
        session.headers['Referer'] = f'{url}'

        response = session.get(url)
        delay = 0.25
        time.sleep(delay)

        like = get_like_from_distro(likes)

        # article emoji url
        # url2 = f'https://ria.ru/services/article/add_emoji/?article_id={article_id}&emotion={like}'

        # comment emoji url
        url2 = f'https://ria.ru/services/chat/add_emoji/'

        # article_id=1796642669&message_id=62b01587828b0bf611315c17&emotion=s1
        data = {'article_id': f'{article_id}', 'message_id': f'{comment_id}', 'emotion': f'{like}'}

        response = session.post(url2, data=data)

        # print('********************')
        # print(response.headers)
        print('********************')
        print(f'{data}')
        print(f'loop: {i}, like: {like}, status_code: {response.status_code}')
        print('********************')
        print(response.text)


def get_like_from_distro(distro='s1:2, s3:1', k=1):
    tmp = distro.split(',')

    likes = []
    weights = ()
    for i in tmp:
        kv = i.strip().split(':')
        likes.append(kv[0])
        weights = weights + (float(kv[1]),)

    #print('LIKES WEIGHTS XXXXXXXXXXXX')
    #print(likes)
    #print(weights)
    #print('XXXXXXXXXXXX')

    res = random.choices(likes, weights = weights, k=k)
    #print(res)
    return res[0]


def test_get_like_from_distro():
    res = get_like_from_distro(distro='s1:3, s2:2, s3:1', k=10)
    print(res)


def test_choice():
    for i in range(9):
        print(random.choice(['s2', 's4', 's5', 's6']))
        #print(random.randrange(1, 4, 1))


def test_ec2_action(ec2_end_action = 'stop', apply_ec2_end_action = False):
    print(f'action: {ec2_end_action}, apply: {apply_ec2_end_action}')
    ec2.terminate_self(action = ec2_end_action, apply_action = apply_ec2_end_action)


def test_multi():
    urls, like_distro, loops_distro, ec2_end_action, apply_ec2_end_action = params.get_params_for_comment()

    for i in range(len(urls)):
        url = urls[i]
        loops = loops_distro[i]
        like_distro_str = like_distro[i]

        print(f'i: {i}, loops: {loops_distro}, like_distro_str: {like_distro_str}')
        article_id = parse.parse_qs(parse.urlparse(url).query)['chat_room_id'][0]
        comment_id = parse.parse_qs(parse.urlparse(url).query)['chat_message_id'][0]

        for j in range(loops):
            like = get_like_from_distro(like_distro_str)
            print(f'like from distro: {like}')


def test_main():
    main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    #test_main()



