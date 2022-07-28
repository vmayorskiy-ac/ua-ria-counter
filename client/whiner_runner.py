import json

import runner


def main(specs_file_name='specs/whiner.json',
         param_name='/ria/whiner/params',
         launch_template_id='lt-093df9412818abd25'):

    instance_count, launch, specs_json = runner.build_specs(specs_file_name=specs_file_name)
    specs = json.dumps(specs_json, indent=4)

    runner.run(specs=specs,
               param_name=param_name,
               launch_template_id=launch_template_id,
               instance_count=instance_count,
               launch=launch)


def test_build_specs():
    res = runner.build_specs()
    print(res)


if __name__ == '__main__':
    main()
    #test_build_specs()
