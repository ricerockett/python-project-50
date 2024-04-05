import os
from gendiff.gendiff import generate_diff, get_common_keys, open_file

file1_path = 'tests/fixtures/file1.json'
file2_path = 'tests/fixtures/file2.json'
expected_diff = 'tests/fixtures/expected_diff'


def get_path(file):
    return os.path.abspath(file)


def get_two_dicts():
    dict1 = open_file(get_path(file1_path))
    dict2 = open_file(get_path(file2_path))
    return dict1, dict2


def test_generate_diff():
    expected = open(get_path(expected_diff), 'r').read()
    result = generate_diff(get_path(file1_path), get_path(file2_path))
    assert expected == result


def test_get_common_keys():
    expected = {'changed': ['timeout'], 'unchanged': ['host']}
    dict1, dict2 = get_two_dicts()
    result = get_common_keys(dict1, dict2)
    assert expected == result
