#! usr/bin/env python3

import argparse
from gendiff.gendiff import generate_diff


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('dest_file1', metavar='first_file')
parser.add_argument('dest_file2', metavar='second_file')
parser.add_argument('-f', '--format')
args = parser.parse_args()


def main():
    print(generate_diff(args.dest_file1, args.dest_file2))


if __name__ == '__main__':
    main()
