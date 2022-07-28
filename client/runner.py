import pprint
import boto3
import json
import comments


ec2_client = boto3.client('ec2', region_name='us-east-1')
ssm_client = boto3.client('ssm')


def run(specs,
        param_name,
        launch_template_id,
        instance_count,
        launch):

    print(f'instance_count: {instance_count}')
    update_specs(specs=specs, param_name=param_name)

    if launch and instance_count > 0:
        launch_instances(count=instance_count, launch_template_id=launch_template_id)

def build_specs(specs_file_name):
    with open(specs_file_name, 'r', encoding="utf8") as file:
        specs_str = file.read()
    specs_json = json.loads(specs_str)

    instance_count = specs_json['instance_count']
    launch = bool(specs_json['launch_instances'] == 'True')

    del specs_json['instance_count']
    del specs_json['launch_instances']

    return instance_count, launch, specs_json


def launch_instances(count, launch_template_id):
    lt_specifics = {
        'LaunchTemplateId': launch_template_id
    }

    launched_instances = ec2_client.run_instances(MaxCount=count, MinCount=count, LaunchTemplate=lt_specifics)
    print(f"instances launched: {len(launched_instances['Instances'])}")


def update_specs(specs, param_name):
    #name = '/ria/comment/params'
    params = get_param(name = param_name)
    update_param(name=param_name, value=specs)
    pprint.pprint(specs)


def get_param(name):
    parameter = ssm_client.get_parameter(Name=name)
    return parameter['Parameter']['Value']

def update_param(name, value):
    ssm_client.put_parameter(
        Name=name,
        Overwrite=True,
        Value=value,
    )

def test_build_specs():
    res = build_specs()
    print(res)


if __name__ == '__main__':
    run(launch_template_id='lt-094fa1f23c82c5f08')
    #test_build_specs()
