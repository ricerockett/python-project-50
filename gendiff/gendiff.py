import json


def open_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def generate_diff(file1, file2):
    file1, file2 = open_json(file1), open_json(file2)
    result = []

    for key in file1:
        if key in file2:

            if file1[key] == file2[key]:
                result.append(f'  {key}: {file1[key]}')
            else:
                result.append(f'- {key}: {file1[key]}')
                result.append(f'+ {key}: {file2[key]}')
            file2.pop(key)

        else:
            result.append(f'- {key}: {file1[key]}')

    for key in file2:
        result.append(f'+ {key}: {file2[key]}')

    return '\n'.join(result)
