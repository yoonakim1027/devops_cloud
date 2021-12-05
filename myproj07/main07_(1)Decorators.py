#### 장식자 (Decorators)
# 뭔가를 꾸미는 것 !

"""
장식자는? 어떤 함수를 감싸는 목적의 함수(Wrapping)
- 프로그래밍 언어에서는 1급 함수라는 것이 존재 (First class function)
- 하나의 함수를 변수처럼 취급할 수 있는 것 

- 변수는 아무때나 만들 수 있다
- 그 만든 변수를 대입해서 새로운 변수를 만들 수도 있음
- 함수에 대한 인자로 변수값을 인자로 넣을 수도 있음! 
- 변수에 대한 값을 리턴할 수 있다. return

<< 변수 >>
- 변수는 동적으로 생성될 수 있다.
- 다른 변수에 대입하여, 새로운 변수를 생성할 수 있다.
- 변수는 함수의 인자로 넘길 수 있다.
- 변수는 함수의 리턴값으로 사용될 수 있다.

<< 함수 >>
- 함수는 동적으로 생성될 수 있다.
- 다른 함수에 대입하여, 새로운 변수(함수)를 생성할 수 있다.
- 함수는 다른 함수의 인자로 넘길 수 있다.
- 함수는 다른 함수의 리턴값으로 사용될 수 있다.
** 함수도 하나의 타입이다 ! 

=> 이를 지원하는 프로그래밍 언어는 '1급함수'를 지원하는 언어라고 할 수 있음



First Class Function (일급 함수)
변수는 동적으로 생성될 수 있다.
다른 변수에 대입하여, 새로운 변수를 생성할 수 있다.
변수는 함수의 인자로 넘길 수 있다.
변수는 함수의 리턴값으로 사용될 수 있다.
함수는 동적으로 생성될 수 있다.
다른 변수에 함수를 대입하여, 새로운 변수(함수)를 생성할 수 있다.
함수는 함수의 인자로 넘길 수 있다.
함수는 함수의 리턴값으로 사용될 수 있다.
=> 이를 지원하는 언어는 "일급함수"를 지원하는 언어라 할 수 있습니다
"""

name = "Tom"  # 좌항에서 우항에 있는 것을 가져가는 것
mysum = lambda x, y: x + y  # 변수 인데, type이 함수인 것
# 함수기 때문에


other_name = name  # - 그 만든 변수를 대입해서 새로운 변수를 만들 수도 있음
other_fn = mysum  # 다른 이름의 변수에 함수를 할당할 수 있다.
other_fn(1, 2)  # 3이 리턴될 것!


def fn(x):
    y = "hello"
    return y  # 변수에 대한 값을 리턴할 수 있다. return


fn(name)  # 함수에 대한 인자로 변수값을 인자로 넣을 수도 있음!


### 함수 만들기

## 1
def base_10():
    number = 10
    return number  # 변수는 리턴될 수 있음.


a = base_10()  # a를 출력하면 a는 10일 것!
other_fn = base_10()

## 2
def base_10():
    fn = lambda x, y: x + y + 10  # 2개의 인자를 받으면 2개 값과 10을 더한 값을 리턴
    return fn  # 함수 리턴


print(other_fn(1, 2))


# 위에거랑 같은 식!!
## 3. 함수안의 지역변수 (Local variable)
def base_10():
    def fn(x, y):  # 호출 될때 마다 fn이라는 새로운 함수가 생성되는 것!
        return x + y + 10  # 2개의 인자를 받으면 2개 값과 10을 더한 값을 리턴

    return fn  # 함수 리턴


other_fn = base_10()
print(other_fn(1, 2))


###4
def base(base_number):  # 인자 하나를 받음
    def fn(x, y):  # 호출 될때 마다 fn이라는 새로운 함수가 생성되는 것!
        return x + y + base_number
        # 2개의 인자를 받으면 2개 값과 base_number를 더한 값을 리턴

    return fn  # 함수 리턴


base_10 = base(10)  # base를 10으로 지정했기 때문에 이게 base_number가 됨
print(base_10(1, 2))

base_20 = base(20)
print(base_20(1, 2))

#### 함수를 통해서 새로운 함수를 만들기
"""
- 함수라는 것은 우리가 매번 모든 함수를 개발하는 것이 X
- 함수를 통해서 새로운 함수를 만들어낼 수 있음
- 이런 동적인 기능이 들어가면? 
- 

"""


### time
import time


def mysum2(x, y):
    time.sleep(1)  # 1초간 대기
    return x + y + 10


print(mysum2(1, 2))  # 1초씩 대기 후 출력
print(mysum2(1, 2))
print(mysum2(1, 2))

# 인자가 같으면 항상 리턴값이 같다는 것을 암

# 인자에 대한 리턴값을 저장
# key : 인자 값에 대한 튜플
# value : 그 인자로 함수를 수행했을 때의 리턴값

cached = {}  # 밖에다 쓰는 것은 전역 함수 (근데 이것은 가급적 지양해야 함! )
# 함수 안에 있는 변수 말고, 함수 밖에 있는 전역 변수는 정말 안써야 함


def mysum2(x, y):
    key = (x, y)  # 튜플은 한 개의 값
    if key not in cached:  # 키 인자로서 이 함수가 계산(수행)된 적이 없다면?
        time.sleep(1)  # 1초간 대기
        cached[key] = x + y + 10  # 없다면? 계산하고 key에 저장
    return cached[key]

    # 계산하고 수행결과를 cashed에 저장


print(mysum2(1, 2))  # 1초씩 대기 후 출력
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 2))  # 첫번째 줄에서 계산된 결과를 쓴 것 !
print(mysum2(1, 2))

# 위에것보다 빠른 결과가 나옴!!
# 위에 것은 더한 결과


def mymultiply2(x, y):
    time.sleep(1)  # 시간이 1초 걸림
    return x * y + 10


print(mysum2(1, 2))  # 1초씩 대기 후 출력
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 2))  # 첫번째 줄에서 계산된 결과를 쓴 것 !
print(mysum2(1, 2))

# 인자가 호출되면 무조건 1초씩 걸림
# 그럼 밑에 5개니까 5초 걸릴거야
print(mymultiply2(1, 2))
print(mymultiply2(1, 3))
print(mymultiply2(1, 3))
print(mymultiply2(1, 2))


# 구현을 어떻게 하냐에 따라,
# 호출하는 쪽은 똑같은데,
cached2 = {}  # 2를 위한 cached 사전을 또 만드는 것


def mymultiply2(x, y):
    key = (x, y)
    if key not in cached2:
        time.sleep(1)  # 시간이 1초 걸림
        cached2[key] = x * y + 10
    return cached2[key]


# cached라는 같은 공간에 저장!
# 그래서 (1,2)에 대한 계산결과를 13이라고 저장함
# 근데 그래서 위의 결과를 그대로 출력한 것임
# 그래서 캐싱할때도 어디에 저장할 것인지 잘 생각해야 함!
