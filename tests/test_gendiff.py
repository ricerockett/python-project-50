import os
from gendiff.gendiff import generate_diff, open_json

file1_path = os.path.abspath('tests/fixtures/file1.json')
file2_path = os.path.abspath('tests/fixtures/file2.json')


expected = '''  host: hexlet.io
- timeout: 50
+ timeout: 20
- proxy: 123.234.53.22
- follow: False
+ verbose: True'''

expected_file1_content = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}


def test_open_json():
    result = open_json(file1_path)
    assert result == expected_file1_content


def test_generate_diff():
    result = generate_diff(file1_path, file2_path)
    assert result == expected
