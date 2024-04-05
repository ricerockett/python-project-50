import json


def open_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def get_sorted_keys(file1, file2):
    return sorted(list(set(file1) | set(file2)))


def get_common_unchanged_keys(file1, file2):
    common_keys = set(file1) & set(file2)
    return list(filter(lambda key: file1[key] == file2[key], common_keys))


def get_common_changed_keys(file1, file2):
    common_keys = set(file1) & set(file2)
    return set(filter(lambda key: file1[key] != file2[key], common_keys))


def get_deleted_keys(file1, file2):
    return set(file1) - set(file2)


def get_added_keys(file1, file2):
    return set(file2) - set(file1)


def generate_diff(file1, file2):
    file1, file2 = open_json(file1), open_json(file2)
    ordered_keys = get_sorted_keys(file1, file2)
    unchanged_keys = get_common_unchanged_keys(file1, file2)
    changed_keys = get_common_changed_keys(file1, file2)
    deleted_keys = get_deleted_keys(file1, file2)
    added_keys = get_added_keys(file1, file2)
    result = []
    for key in ordered_keys:
        if key in unchanged_keys:
            result.append(f'  {key}: {file1[key]}')
        elif key in changed_keys:
            result.append(f'- {key}: {file1[key]}')
            result.append(f'+ {key}: {file2[key]}')
        elif key in deleted_keys:
            result.append(f'- {key}: {file1[key]}')
        elif key in added_keys:
            result.append(f'+ {key}: {file2[key]}')
    return '\n'.join(result)
