import pytest
from . import numbers_add

@pytest.mark.parametrize("input, expected", [
    ("숫자더하기: 1, 2, 3", 6),
    ("숫자더하기: 100, 200, 300", 600),
])
def test_numbers_add(input, expected):
    assert numbers_add.check_available(input)
    assert numbers_add.make_response(input) == str(expected)
