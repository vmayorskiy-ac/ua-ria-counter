import pprint
import boto3
import json
import comments
import os
import runner
import time


def worker(dir_path='bak/20220718'):
    spec_files = os.listdir(dir_path)
    print(spec_files)

    for spec_file_name in spec_files:
        print('************************')
        print(spec_file_name)
        runner.run(specs_file_name=f'{dir_path}/{spec_file_name}')
        time.sleep(60)


    #with open('specs.json', 'r', encoding="utf8") as file:
    #    specs_str = file.read()


def test_worker():
    worker()


if __name__ == '__main__':
    #worker()
    test_worker()
