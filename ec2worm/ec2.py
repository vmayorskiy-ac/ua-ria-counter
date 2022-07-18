import boto3
import requests
import pprint
import time
from urllib import parse

import requests


def terminate_self(action, apply_action = False):
    response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
    instance_id = response.text
    dry_run = not apply_action
    print(f'instance_id: {instance_id}, dry_run: {dry_run}')
    ec2 = boto3.resource('ec2', region_name = 'us-east-1')
    instance = ec2.Instance(instance_id)

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


