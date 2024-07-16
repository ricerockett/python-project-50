import yaml
import json
from stylish import format_diff_tree


def open_file(path):
    with open(path, 'r') as file:
        if path.endswith('.yaml') or path.endswith('.yml'):
            data = yaml.load(file, Loader=yaml.Loader)
        elif path.endswith('.json'):
            data = json.load(file)
        return data


def get_diff_tree(data1, data2):
    result = {}
    for key in sorted(data1.keys() | data2.keys()):
        value1, value2 = data1.get(key), data2.get(key)
        if key not in data1:
            result[key] = {'type': 'added',
                           'value': value2}
        elif key not in data2:
            result[key] = {'type': 'deleted',
                           'value': value1}
        elif isinstance(value1, dict) and isinstance(value2, dict):
            result[key] = {'type': 'parent',
                           'children': get_diff_tree(value1, value2)}
        elif value1 != value2:
            result[key] = {'type': 'changed',
                           'old_value': value1,
                           'new_value': value2}
        else:
            result[key] = {'type': 'unchanged',
                           'value': value1}
    return result



def generate_diff():
    data1, data2 = open_file(), open_file()
    diff = get_diff_tree(data1, data2)
    return format_diff_tree(diff)

