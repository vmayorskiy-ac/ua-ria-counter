import json
import comments

import runner


def main(specs_file_name='specs/comments.json',
         param_name='/ria/comment/params',
         launch_template_id='lt-094fa1f23c82c5f08'):

    instance_count, launch, specs_json = runner.build_specs(specs_file_name=specs_file_name)
    specs = customize_specs(specs_json)

    runner.run(specs=specs,
               param_name=param_name,
               launch_template_id=launch_template_id,
               instance_count=instance_count,
               launch=launch)


def customize_specs(specs_json):
    urls, likes, good_like_counts = comments.get_comment_urls(article_id=specs_json['article_id'],
                                                              comment_quotes=specs_json['comment_quotes'],
                                                              negatives=specs_json['negatives'])

    specs_json['urls'] = urls
    specs_json['likes'] = likes
    specs_json['good_like_counts'] = good_like_counts
    print(good_like_counts)

    del specs_json['comment_quotes']
    del specs_json['template']
    del specs_json['negatives']

    specs = json.dumps(specs_json, indent=4)
    return specs


def test_build_specs():
    res = runner.build_specs()
    print(res)


if __name__ == '__main__':
    main()
    #test_build_specs()
