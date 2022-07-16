import boto3
import sys
import requests
import pprint
import time
from urllib import parse

import requests


def terminate_self(action, dry_run = True):
    response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
    instance_id = response.text
    print(f'instance_id: {instance_id}, dry_run: {dry_run}')
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(id)

    if(action == 'stop'):
        print('stop')
        if(not dry_run):
            print('not dry run')
            print(instance.stop())
    elif(action == 'terminate'):
        print('terminate')
        if(not dry_run):
            print('not dry run')
            print(instance.terminate())
    else:
        print('unknown action')
        if(not dry_run):
            print('not dry run')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    terminate_self('foo')


