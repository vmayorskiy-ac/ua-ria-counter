import pprint
import boto3
import json
import comments

import runner


ec2_client = boto3.client('ec2', region_name='us-east-1')
ssm_client = boto3.client('ssm')


def main(specs_file_name='specs/comments.json',
         param_name='/ria/comment/params',
         launch_template_id='lt-094fa1f23c82c5f08'):

    instance_count, launch, specs = build_specs(specs_file_name=specs_file_name)

    runner.run(specs=specs,
               param_name=param_name,
               launch_template_id=launch_template_id,
               instance_count=instance_count,
               launch=launch)


def build_specs(specs_file_name):
    with open(specs_file_name, 'r', encoding="utf8") as file:
        specs_str = file.read()
    specs_json = json.loads(specs_str)

    urls, likes, good_like_counts = comments.get_comment_urls(article_id=specs_json['article_id'],
                                                              comment_quotes=specs_json['comment_quotes'],
                                                              negatives=specs_json['negatives'])

    specs_json['urls'] = urls
    specs_json['likes'] = likes
    specs_json['good_like_counts'] = good_like_counts
    print(good_like_counts)

    instance_count = specs_json['instance_count']
    launch = bool(specs_json['launch_instances'] == 'True')

    del specs_json['comment_quotes']
    del specs_json['template']
    del specs_json['negatives']

    return instance_count, launch, json.dumps(specs_json, indent=4)


def test_build_specs():
    res = build_specs()
    print(res)


if __name__ == '__main__':
    main(launch_template_id='lt-094fa1f23c82c5f08')
    #test_build_specs()
