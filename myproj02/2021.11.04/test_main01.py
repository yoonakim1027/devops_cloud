import pytest

from main01 import get_word_count
from main01 import get_ch_count_except_space
from main01 import get_rounded_number

# 문자열로 sentence, expected -> 한 문자열로 부여됨
@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("우리는 파이썬을 즐겨요", 3),
        ("Python Family", 2),
    ],
)
def test_get_word_count2(sentence, expected):
    assert get_word_count(sentence) == expected


## test할때 def다음에 올 이름이 같으면 덮어씌워짐!!
## test명도 다르게 지정해야 함

# 꼭 test할때는 test_를 붙여야함!
#
#
#####  @pytest.mark.parametrize("",[])
# 이게 기본값!!

##### @pytest.mark.parametrize("값",[예상하는 값])
@pytest.mark.parametrize(
    "number, expected",
    [(1234567, 1234000), (1234, 1000)],
)
def test_get_rounded_number2(number, expected):
    assert get_rounded_number(number) == expected


# 숫자를 하드코딩 하지 않고 이 인자를 넘겨주면 됨 .


def test_get_word_count_():  # 지금은 하나가 있는 셈 !
    assert get_word_count("우리는 파이썬을 즐겨요") == 3
    assert get_word_count("Python Family") == 2


def test_get_ch_count_except_space():  # def 다음에는 test_ 붙이고
    assert get_ch_count_except_space("우리는 파이썬을 즐겨요") == 10  # assert에는 안붙임
    assert get_ch_count_except_space("Python Family") == 12


# assert는 파이썬의 문법.
# assert 뒤의 것이 참인지를 확인하는 함수


# (input,output)
# 하나의 테스트 안에 두개의 assert가 있을뿐 총 테스트는 3개인 셈 !
def test_get_rounded_number():
    assert get_rounded_number(1234567) == 1234000
    assert get_rounded_number(1234) == 1000


# 테스트를 통해서 얻을 수 있는건 마음의 안정감..^^
# 그런데 테스트에서 에러가 안나온다고 해서 버그가 없다는것은 아님
# 테스트가 실패했을 경우, 에러가 있을 확률이 더 높다는 것
