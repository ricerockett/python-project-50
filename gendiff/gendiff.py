import json


def open_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def get_common_unchanged_keys(file1, file2):
    common_keys = set(file1) & set(file2)
    return list(filter(lambda key: file1[key] == file2[key], common_keys))


def get_common_changed_keys(file1, file2):
    common_keys = set(file1) & set(file2)
    return set(filter(lambda key: file1[key] != file2[key], common_keys))


def generate_diff(file1, file2):
    data1, data2 = open_json(file1), open_json(file2)
    unchanged_keys = get_common_unchanged_keys(data1, data2)
    changed_keys = get_common_changed_keys(data1, data2)
    result = []
    for key in sorted(data1.keys() | data2.keys()):
        if key in unchanged_keys:
            result.append(f'  {key}: {data1[key]}')
        elif key in changed_keys:
            result.append(f'- {key}: {data1[key]}')
            result.append(f'+ {key}: {data2[key]}')
        elif key in (data1.keys() - data2.keys()):
            result.append(f'- {key}: {data1[key]}')
        elif key in (data2.keys() - data1.keys()):
            result.append(f'+ {key}: {data2[key]}')
    return '\n'.join(result)
