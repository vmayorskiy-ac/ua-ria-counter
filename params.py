import random
import boto3
import requests
import pprint
import time
from urllib import parse
import json


def get_params_for_comment():
    ssm = boto3.client('ssm', region_name='us-east-1')
    param = ssm.get_parameter(Name='/ria/comment/params')
    param_json = param['Parameter']['Value'].strip()

    print(param_json)

    param_dict = json.loads(param_json)

    pprint.pprint(param_dict)

    comment_url = param_dict['url']
    article_id = parse.parse_qs(parse.urlparse(comment_url).query)['chat_room_id'][0] 
    message_id = parse.parse_qs(parse.urlparse(comment_url).query)['chat_message_id'][0] 

    like = param_dict['like'] 
    loops = param_dict['loops']
    ec2_end_action = param_dict['ec2_end_action'] 
    apply_ec2_end_action = param_dict['apply_ec2_end_action'] == 'True'
    #loops = int(param['Parameter']['Value'].strip())
    return comment_url, article_id, message_id, like, loops, ec2_end_action, apply_ec2_end_action


def get_params_for_comment_old():
    ssm = boto3.client('ssm', region_name='us-east-1')
    param = ssm.get_parameter(Name='/ria/comment/url')
    comment_url = param['Parameter']['Value'].strip()
    #url = 'https://ria.ru/20220620/kuleba-1796642669.html?chat_message_id=62b01587828b0bf611315c17&chat_room_id=1796642669'

    article_id = parse.parse_qs(parse.urlparse(comment_url).query)['chat_room_id'][0] 
    message_id = parse.parse_qs(parse.urlparse(comment_url).query)['chat_message_id'][0] 

    param = ssm.get_parameter(Name='/ria/comment/like')
    like = param['Parameter']['Value'].strip()
    param = ssm.get_parameter(Name='/ria/comment/loops')
    loops = int(param['Parameter']['Value'].strip())
    return comment_url, article_id, message_id, like, loops


def get_params():
    ssm = boto3.client('ssm', region_name='us-east-1')
    param = ssm.get_parameter(Name='/ria/article_url')
    article_url = param['Parameter']['Value'].strip()
    #article_id = 'https://ria.ru/20220619/bespilotnik-1796545591.html'
    article_id = article_url[-15:-5]

    param = ssm.get_parameter(Name='/ria/like')
    like = param['Parameter']['Value'].strip()
    param = ssm.get_parameter(Name='/ria/loops')
    loops = int(param['Parameter']['Value'].strip())
    return article_url, article_id, like, loops


def test_comment_url():
    article_url, article_id, comment_id, like, loops, ec2_end_action, apply_ec2_end_action = get_params_for_comment()
    print(article_url)
    print(article_id)
    print(comment_id)
    print(like)
    print(loops)
    print(ec2_end_action)
    print(apply_ec2_end_action)
    

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #main()
    test_comment_url()



