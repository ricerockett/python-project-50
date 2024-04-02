#! usr/bin/env python3

import argparse
import json
import copy


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('dest_file1', metavar='first_file')
parser.add_argument('dest_file2', metavar='second_file')
parser.add_argument('-f', '--format')
args = parser.parse_args()


def open_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def generate_diff(file1, file2):
    file1 = open_json(file1)
    file2 = copy.deepcopy(open_json(file2))
    common_keys = []
    result = ''
    for key in file1:
        if key in file2:
            if file1[key] == file2[key]:
                result += f'  {key}: {file1[key]} \n'
                common_keys.append(key)
            else:
                result += f'- {key}: {file1[key]} \n'
                result += f'+ {key}: {file2[key]} \n'
                common_keys.append(key)
        else:
            result += f'- {key}: {file1[key]} \n'

    for key in common_keys:
        file2.pop(key)
    for key in file2:
        result += f'+ {key}: {file2[key]} \n'
    return result


def main():
    print(generate_diff(args.dest_file1, args.dest_file2))


if __name__ == '__main__':
    main()

