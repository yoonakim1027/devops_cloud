from . import reverse_string


# 문자열에서
def test_reverse_string():
    assert reverse_string.check_available("거꾸로: 안녕")
    assert reverse_string.make_response("거꾸로: 안녕") == "녕안"

# assert 단언 -> 참이 아니면 출력하지 않는다.
# test를 이용하는 것이 test 주도하는 방법

# 연습하기
