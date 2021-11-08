from main06 import make_powered_list


# 이 테스트가 이 함수에 대한 스펙(요구사항)
# 테스트만으로 이 함수의 동작을 한번에 알 수 있는 것
# 나중에 유지보수 할 때 빠른 피드백이 가능함
def test_make_powered_list():
    numbers = [0, 1, 2, 3, 4]
    expected = [0, 1, 4, 9, 16]
    assert make_powered_list(numbers) == expected
