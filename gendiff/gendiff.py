import json


def open_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def get_sorted_keys(file1, file2):
    return sorted(list(set(file1) | set(file2)))


def generate_diff(file1, file2):
    file1, file2 = open_json(file1), open_json(file2)
    ordered_keys = get_sorted_keys(file1, file2)
    result = []

    for key in ordered_keys:
        if key in file1 and key in file2 and file1[key] == file2[key]:
            result.append(f'  {key}: {file1[key]}')
        elif key in file1 and key in file2 and file1[key] != file2[key]:
            result.append(f'- {key}: {file1[key]}')
            result.append(f'+ {key}: {file2[key]}')
        elif key in file1 and key not in file2:
            result.append(f'- {key}: {file1[key]}')
        elif key in file2 and key not in file1:
            result.append(f'+ {key}: {file2[key]}')

    return '\n'.join(result)
