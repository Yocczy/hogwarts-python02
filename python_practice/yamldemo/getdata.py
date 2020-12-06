import yaml


def get_data():
    with open('data.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas


print(get_data())
