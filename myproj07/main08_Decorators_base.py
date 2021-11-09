# 장식자의 첫번째 인자는 항상 내가 꾸밀 함수를 인자로 받음


def base(base_number):
    def wrap(fn):  # 장식장 이름
        def inner(x, y):  # 위에랑 밑에랑 받는 함수인자 갯수가 똑같아야함. 위에것을 감싸서 받는거라
            return fn(x, y) + base_number  # 인수로 받으면 원래 함수를 호출해서 계산결과 나타냄

        return inner  # 정의한 이름과 리턴한 이름만 같으면 돼

    return wrap


# 참조하고 있는 함수의 이름만 바꿨을 뿐 로직은 같음

base_10 = base(10)  # 위의 함수는? base_10이랑 같은 것
# 아래의 base()를 직접한것과 base_10에 저장한거랑 같은것
# base_10이라는 장식장에 넣는 것

base_20 = base(20)
base_100 = base(100)


# def base_10(fn):  # 장식장 이름
#     def wrap(x, y):  # 위에랑 밑에랑 받는 함수인자 갯수가 똑같아야함. 위에것을 감싸서 받는거라
#         return fn(x, y) + 10  # 인수로 받으면 원래 함수를 호출해서 계산결과 나타냄

#     return wrap


# @base_10  # 장식장 사용은 @다음에 장식장(함수)이름
# @base_10  # 이렇게 두 개 깔면 10이 또 추가됨
# def mysum2(x, y):
#     return x + y


# print(mysum2(1, 2))


# def base_20(fn):  # 장식장 이름
#     def wrap(x, y):  # 위에랑 밑에랑 받는 함수인자 갯수가 똑같아야함. 위에것을 감싸서 받는거라
#         return fn(x, y) + 20  # 인수로 받으면 원래 함수를 호출해서 계산결과 나타냄

#     return wrap


# @base_10  # 장식장 사용은 @다음에 장식장(함수)이름
# @base_20  # 이렇게 두 개 깔면 10이 또 추가됨
# def mysum2(x, y):
#     return x + y


# def mymultiply2(x,y):
#     return x * y
