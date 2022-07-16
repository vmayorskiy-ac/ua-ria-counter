import random
import boto3
import requests
import pprint
import time
from urllib import parse


def main():
    #url = 'https://ria.ru'
    #article_id = '1796174981'
    #loops = 9
    #like = 's6'
    url, article_id, comment_id, like, loops = get_params_for_comment()

    for i in range(loops):
        for j in [1]:
            time.sleep(1.25)
            response = requests.get(url)

            session = requests.Session()
            session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0'
            session.headers['Origin'] = 'https://ria.ru'
            session.headers['Referer'] = f'{url}'

            response = session.get(url)
            delay = random.randrange(1, 4, 1)
            #delay = 1.25
            time.sleep(delay)

            # article emoji url
            #url2 = f'https://ria.ru/services/article/add_emoji/?article_id={article_id}&emotion={like}'

            # comment emoji url
            url2 = f'https://ria.ru/services/chat/add_emoji/'
            
            # article_id=1796642669&message_id=62b01587828b0bf611315c17&emotion=s1
            #data = f'article_id={article_id}&message_id={comment_id}&emotion={like}'
            data = { 'article_id': f'{article_id}', 'message_id': f'{comment_id}', 'emotion': f'{like}' }
            response = session.post(url2, data=data)

            #print('********************')
            #print(response.headers)
            print('********************')
            print(f'loop: {i}, like: {like}, status_code: {response.status_code}')
            print('********************')
            print(response.text)


def get_params_for_comment():
    ssm = boto3.client('ssm', region_name='us-east-1')
    param = ssm.get_parameter(Name='/ria/comment_url')
    comment_url = param['Parameter']['Value']
    #url = 'https://ria.ru/20220620/kuleba-1796642669.html?chat_message_id=62b01587828b0bf611315c17&chat_room_id=1796642669'

    article_id = parse.parse_qs(parse.urlparse(comment_url).query)['chat_room_id'][0] 
    message_id = parse.parse_qs(parse.urlparse(comment_url).query)['chat_message_id'][0] 

    param = ssm.get_parameter(Name='/ria/like')
    like = param['Parameter']['Value']
    param = ssm.get_parameter(Name='/ria/loops')
    loops = int(param['Parameter']['Value'])
    return comment_url, article_id, message_id, like, loops


def get_params():
    ssm = boto3.client('ssm', region_name='us-east-1')
    param = ssm.get_parameter(Name='/ria/article_url')
    article_url = param['Parameter']['Value']
    #article_id = 'https://ria.ru/20220619/bespilotnik-1796545591.html'
    article_id = article_url[-15:-5]

    param = ssm.get_parameter(Name='/ria/like')
    like = param['Parameter']['Value']
    param = ssm.get_parameter(Name='/ria/loops')
    loops = int(param['Parameter']['Value'])
    return article_url, article_id, like, loops


def test_comment_url():
    article_url, article_id, comment_id, like, loops = get_params_for_comment()
    print(article_url)
    print(article_id)
    print(comment_id)
    print(like)
    print(loops)
    

def test_article_url():
    article_url, article_id, like, loops = get_params()
    print(article_url)
    print(article_id)
    print(like)
    print(loops)
    

def test_ssm():
    article_id, like, loops = get_params()
    print(article_id)
    print(like)
    print(loops)


def test_choice():
    for i in range(9):
        print(random.choice(['s2', 's4', 's5', 's6']))
        #print(random.randrange(1, 4, 1))

def test_eip():
    client = boto3.client('ec2', region_name='us-east-1')
    eip = {}
    addresses_dict = client.describe_addresses()
    for eip_dict in addresses_dict['Addresses']:
        print(eip_dict['PublicIp'])
        val = eip_dict['Tags'][0]['Value']
        print(val)
        if val == 'v-dev-test':
            eip = eip_dict

    pprint.pprint(eip)
    #client.disassociate_address(PublicIp = eip['PublicIp'])
    #client.associate_address(PublicIp = eip['PublicIp'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    #test_comment_url()



