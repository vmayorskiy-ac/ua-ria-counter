import json

import runner
import chat_services


def main(specs_file_name='specs/whiner.json',
         param_name='/ria/whiner/params',
         launch_template_id='lt-093df9412818abd25'):

    instance_count, launch, specs_json = runner.build_specs(specs_file_name=specs_file_name)
    specs = customize_specs(specs_json)

    runner.run(specs=specs,
               param_name=param_name,
               launch_template_id=launch_template_id,
               instance_count=instance_count,
               launch=launch)


def customize_specs(specs_json):
    article_ids = chat_services.get_top_chat_rooms()

    specs_json['article_ids'] = article_ids

    specs = json.dumps(specs_json, indent=4)
    return specs


def test_build_specs():
    res = runner.build_specs()
    print(res)


if __name__ == '__main__':
    main()
    #test_build_specs()
