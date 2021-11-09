### time 아까 그 코드를 개선해보자 !
import time


# def mysum2(x, y):
#     time.sleep(1)  # 1초간 대기
#     return x + y + 10


# print(mysum2(1, 2))  # 1초씩 대기 후 출력
# print(mysum2(1, 2))
# print(mysum2(1, 2))

# 인자가 같으면 항상 리턴값이 같다는 것을 암

# 인자에 대한 리턴값을 저장
# key : 인자 값에 대한 튜플
# value : 그 인자로 함수를 수행했을 때의 리턴값

# cached = {}  # 밖에다 쓰는 것은 전역 함수 (근데 이것은 가급적 지양해야 함! )
# # 함수 안에 있는 변수 말고, 함수 밖에 있는 전역 변수는 정말 안써야 함


# def mysum2(x, y):
#     key = (x, y)  # 튜플은 한 개의 값
#     if key not in cached:  # 키 인자로서 이 함수가 계산(수행)된 적이 없다면?
#         time.sleep(1)  # 1초간 대기
#         cached[key] = x + y + 10  # 없다면? 계산하고 key에 저장
#     return cached[key]

#     # 계산하고 수행결과를 cashed에 저장


##### 수정 #####
### 파이썬의 장식자
## 좀 더 가독성 좋게 개선하자
## 로직은 그대로! 적용하는 방법의 개선!


##### 데코레이터 사용 X


def memoize(fn):  # 인자로 어떤 함수를 받을거임! -> 이 이름을 fn
    cached = {}  # 사전 생성
    # memoize라는 함수가 호출될 때마다 매번 새로운 cached가 만들어진다
    def wrap(x, y):  # memoize가 호출될 때마다 매번 새로운 wrap이 만들어짐
        return fn(x, y)  # 파이썬의 장식자를 구현하는 가장 기본적인 코드

    return wrap  # 리턴된 함수는 내부적으로 인자로 받은 fn을 참조하고 있음


# 매번 wrap라는 함수를 만들어서 새롭게 만듬


def mysum2(x, y):
    time.sleep(1)
    return x + y + 10


other_fn = memoize(mysum2)  # 함수의 호출을 전역에서 함
# 인자를 뭘로 넘겨줄래? -> mysum2라는 함수를 인자로 !
# 호출이 되면, fn -> mysum2
# 이 memoize의 반환값, 리턴값은? other_fn에 저장
other_fn(1, 2)  # -> wrap에서 1,2가 호출되는 것
# 그럼 안에서 mysum2(1,2)를 호출하게 되는 것


# 인자로 넘긴 함수와 같은 이름으로 return값을 받음
# 그럼 이거를 줄여서 어떻게 쓰냐면 ?

mysum2 = memoize(mysum2)  # 2개 이름이 같아서 좀 낯설지만?
# i = 0
# i = i+1 #i의 값을 참조해서 대입해서 값을 넣음
# return을 받을때 좌항을 받음 -> 이 좌항은 wrap과 같은 역할을 하는 것
# memoize를 통해서 새로운 mysum2을 만든 것

mysum2(1, 2)


def memoize(fn):  # 인자로 어떤 함수를 받을거임! -> 이 이름을 fn
    cached = {}  # 사전 생성
    # memoize라는 함수가 호출될 때마다 매번 새로운 cached가 만들어진다
    def wrap(x, y):  # memoize가 호출될 때마다 매번 새로운 wrap이 만들어짐
        key = (x, y)
        if key not in cached:
            cached[key] = fn(x, y)
        return cached[key]  # 파이썬의 장식자를 구현하는 가장 기본적인 코드

    return wrap  #


def mymultiply2(x, y):
    time.sleep(1)
    return x + y + 10


mymultiply2 = memoize(mymultiply2)
# 원래 원본 함수가 아닌, 이를 wrapping하는 새로운 함수를 만듬.
# sum 할때도 인자의 그룹이 2
# 곱하기 할때도 인자의 그룹이 2개
# -> 약 4초가 걸림

# 지금도 위의 mymultiply2는 안건들었는데 성능이 좋아짐~


###### 데코레이터 사용 O
# 인자로 넘긴 함수와 같은 이름으로 return값을 받음
# 그럼 이거를 줄여서 어떻게 쓰냐면 ?
@memoize  # @로 쓰는 것이 데코레이터 문법 -> 가독성 좋게 보여지기 위해 !
def mysum2(x, y):
    time.sleep(1)
    return x + y + 10


@memoize
def mymultiply2(x, y):
    time.sleep(1)
    return x + y + 10


### cached를 공유 X 따로 써야 함!
"""
# 이렇게 @memoize를 쓰는 것은? 
- 전역 변수 없이도, 각각 함수에 대한 인자에 맞춰서 계산 결과를 구현하게 해줌


"""

print(mysum2(1, 2))  # 1초씩 대기 후 출력
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 2))
print(mysum2(1, 2))


print(mymultiply2(1, 2))
print(mymultiply2(1, 3))
print(mymultiply2(1, 3))
print(mymultiply2(1, 2))
