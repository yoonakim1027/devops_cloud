import pytest

from . import numbers_Add


# ("숫자더하기: 입력값, 예상값)


@pytest.mark.parametrize("line, expected",
                         [("숫자더하기: 1, 2, 3", 6),
                          ("숫자더하기: 100, 200, 300", 600),
                          ])
def test_numbers_add(line, expected):
    assert numbers_Add.check_available(line)
    assert numbers_Add.make_response(line) == str(expected)

# 기본적으로 test_ 함수에는 인자가 안들어간다.
