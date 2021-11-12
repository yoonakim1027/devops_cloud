import pytest
@pytest.mark.parametrize("input, expected",
                         [("숫자더하기: 1, 2, 3", 6),
                         ("숫자더하기: 100, 200, 300", 600),
                         ])

from .import numbers_Add


## 이렇게 하면 test케이스 여러개 할 수 있음
def test_numbers_add():
    assert numbers_Add.check_available(input)
    assert numbers_Add.make_response(input) ==str(expected)


# test케이스 2개 (한정)

# def test_numbers_add():
#     input = "숫자더하기: 1, 2, 3"
#     # 기대하는값
#     expected = 6
#     assert numbers_Add.check_available(input)
#     numbers_Add.make_response(input) ==expected
#
#
#     input = "숫자더하기: 100, 200, 300"
#     # 어떤 케이스들이 실패할지 몇 개정도 정해두기
#     expected = 600
#     assert numbers_Add.check_available(input)
#     numbers_Add.make_response(input) ==expected

