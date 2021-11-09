def mysum2(x, y):
    return x + y + 10


# 인자를 더한 값 + 10 -> 리턴


def mysum3(x, y, z):
    return x + y + z + 10


# 인자를 더한 값 + 10 -> 리턴

###### 가변인자 문법
# 인자를 몇 개 받을지는 모르겠지만, 나는 무제한으로 받겠다.
def mysum(*args):  # 함수를 정의할 때 *args 사용-> 인자 0개도 호출, 100개 천개 만개도 호출 가능
    # *args is tuple -> tuple은 다수의 값을 저장할 수 있음
    # 튜플로서 값이 넘어오게 되는 것!
    # 튜플은 변경은 불가능하지만 순회돌면서 사용 가능!
    print("args: ", args)
    return sum(args) + 10  # 이를 다시 호출할 때에는 *안써도 됨


print(mysum())  # 인자 0개
print(mysum(1))  # 인자 1개
print(mysum(1, 2))  # 인자 2개
print(mysum(1, 2, 3))  # 인자 3개


##### 가변인자 사용
#### 0개가 아니라 최소 2개 받고싶다! -> 위치 인자 2개 지정
# 최소 2개는 호출해야 값 나옴~~
def mysum2(x, y, *args):  # 함수를 정의할 때 *args 사용-> 인자 0개도 호출, 100개 천개 만개도 호출 가능
    # *args is tuple -> tuple은 다수의 값을 저장할 수 있음
    # 튜플로서 값이 넘어오게 되는 것!
    # 튜플은 변경은 불가능하지만 순회돌면서 사용 가능!
    print("args: ", args)
    return x + y + sum(args) + 10  # 이를 다시 호출할 때에는 *안써도 됨


print(mysum2())  # 인자 0개
print(mysum2(1))  # 인자 1개
print(mysum2(1, 2))  # 인자 2개
print(mysum2(1, 2, 3))  # 인자 3개

""" 
- 인자가 4,5,6...개여도 동작할 수 있어야 좀 더 유연한 장식자가 된다
- 그래서 내부에서 *args라는 가변인자로 받았음

"""


"""
장식자가 없으면? 받으면 받은데로 뽑혀버리게 됨
이 장식자들의 역할은?
원래 있는 함수를 감싸는 것.


### filter_fn에서 True로 판정된 인자는 alter_value 값으로 대체 해보자
@myfilter(lambda i: i % 2 == 0, 0)
def mysum(a, b, c, d, e):
    return a + b + c + d + e
= 조건(짝수면)에 부합이 되면 0으로 바꿔라


@myfilter(lambda i: i % 2 == 0, 1)
def mymultiply(a, b, c, d, e):
    return a * b * c * d * e

= 조건에 부합이 되면 1로 바꿔라 

"""
