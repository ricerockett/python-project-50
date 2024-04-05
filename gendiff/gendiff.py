import yaml
import json


def open_file(path):
    with open(path, 'r') as file:
        if path.endswith('.yaml') or path.endswith('.yml'):
            data = yaml.load(file, Loader=yaml.Loader)
        elif path.endswith('.json'):
            data = json.load(file)
        return data


def get_common_keys(dict1, dict2):
    common_keys = dict1.keys() & dict2.keys()
    unchanged = list(filter(lambda key: dict1[key] == dict2[key], common_keys))
    changed = list(filter(lambda key: dict1[key] != dict2[key], common_keys))
    return {'unchanged': unchanged, 'changed': changed}


def generate_diff(file1, file2):
    data1, data2 = open_file(file1), open_file(file2)
    result = []
    for key in sorted(data1.keys() | data2.keys()):
        if key in get_common_keys(data1, data2)['unchanged']:
            result.append(f'  {key}: {data1[key]}')
        elif key in get_common_keys(data1, data2)['changed']:
            result.append(f'- {key}: {data1[key]}')
            result.append(f'+ {key}: {data2[key]}')
        elif key in (data1.keys() - data2.keys()):
            result.append(f'- {key}: {data1[key]}')
        elif key in (data2.keys() - data1.keys()):
            result.append(f'+ {key}: {data2[key]}')
    return '\n'.join(result).replace('True', 'true').replace('False', 'false')
