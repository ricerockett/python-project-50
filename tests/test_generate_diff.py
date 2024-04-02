import pytest
from gendiff.scripts.gendiff import generate_diff


resut = '''  host: hexlet.io
- timeout: 50
+ timeout: 20
- proxy: 123.234.53.22
- follow: False
+ verbose: True
'''


assert generate_diff('test/fixtures/file1.json',
                     'test/fixtures/file1.json') == resut
