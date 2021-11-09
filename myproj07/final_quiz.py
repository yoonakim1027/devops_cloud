# myfilter(함수, 가변인자)
def myfilter(filter_fn, alter_value):
    def wrap(fn):  # 감싸기 : 인자로 어떤 함수를 받겠다는 것 그 이름이 fn
        # myfilter가 호출될때마다 새로 wrap함수가 fn인자를 받아서 호출되는 것
        def inner(*args):  # 가변인자 . 그니까 여기에 가변인자가 들어오는 것.
            # TODO # new_args를 적절히 구성해 주세요
            # new_args는 리스트 및 튜플 자료구조가 가능

            # 그니까 args는 내가 받을 숫자들이 되는 것
            # 이제 얘네가 filter_fn에 맞는 지 확인하는 함수를 만들어야 함
            new_args = []  # 새로운 리스트
            for i in args:  # args의 값을 하나씩 i에 할당
                if filter_fn(i) == True:  #  if filter_fn(i): 동일한 뜻
                    i = alter_value
                    new_args.append(i)
                else:
                    new_args.append(i)

            # key : 위에서 받은 가변인자를 리스트에 저장한 곳
            # (2) 이 리스트를 하나하나씩 함수에 대입하는 식을 만들어야 함

            # new_args = args # 그러니까 new_args는 변한 애들이 리스트나 튜플로 나와야 함
            return fn(*new_args)
            # 여기서 보면 fn은 함수(filter_fn)와 alter_value(가변인자)를 받는 것
            # 그래서 fn이라는 함수 값안에 (*new_args)라는 가변 인자를 받는 것.

        # args의 값을 fn 함수로 전달

        return inner

    return wrap


# 짝수 제외 홀수만 더하기
@myfilter(lambda i: i % 2 == 0, 0)  # myfilter(함수, 가변인자)
def mysum(a, b, c, d, e):
    return a + b + c + d + e


# 근까 함수 값이 들어오면 그거에 if True == 0으로 바꿔줘 라는 내용인데,
# 밑에 보면 def mysum(여기는 함수인자 없이 그냥 몇개 인자 받을건지만 나와있음)

# 내가 만들어야 할 myfilter에서 필요한 인자는(함수, 그래서 해당하는 값을 뭘로바꿀래?(숫자))
# 근까 받은 값들을 함수에 하나씩 넣어서 해당하는 값을 바꿀 숫자로 넣어주는 것

# 짝수는 1로 해서 곱하기
@myfilter(lambda i: i % 2 == 0, 1)
def mymultiply(a, b, c, d, e):
    return a * b * c * d * e


# 계산은 그대로 출력이 됨.
print(mysum(1, 2, 3, 4, 5))  # 출력값 = 9
print(mymultiply(1, 2, 3, 4, 5))  # 출력값 = 15
