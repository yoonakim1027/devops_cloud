answer = input("12+23 = ") #input에서 사용하는 것은 prompt -> 입력안내 메시지(써도 되고 안써도 됨)
# input으로 받으면 <문자열>로 받음 
answer = int(answer)

if answer == 35:
    print("정답")
else:
    print("땡!!!")

# answer를 가지고 계산할 목적이라면?
# answer 값 변환은 최대한 빠르게 수행하는 것이 좋다.


###  받는 값이 아무것도 없을 경우, 0으로 처리하는 방법
answer = int(answer or 0)
# 이렇게 설정하면 그냥 값을 입력하지 않고 엔터만 쳤을 경우, 0으로 처리되게 됨

# if 조건문 : -> 참 거짓 판단. 

if 100:
    print('t')
else :
    print("f")


if 0:
    print('t')
else :
    print("f")


if "hello":
    print('t')
else :
    print("f")


# bool (True/False)
# bool 타입의 값이 아니더라도, bool 판단에 사용될 수 있습니다.
# 숫자 : 0 은 거짓, 0 이외의 모든 값은 True
# 문자열 : 빈 문자열은 거짓, else True


### answer = int(answer or 0)
# or -> 앞선 값이 거짓이면, 콤마 뒤의 값을 대신 사용하겠다.

# len() -> 길이 체크 함수
# if len(answer) == 0:
#     answer = 0
# else:
#     answer = int(answer)
## 근데 이렇게 코딩은 잘 안함 ~ 
# answer = int(answer or 0) -> 파이썬은 이런 식으로 코딩 많이함 


#range() -> 등차수열목록을 만들어주는 함수
# randint(이상,이하) -> 1개 값을 뽑아줌.
# randint((이상,미만),몇개 뽑을래?)

import random
for i in range(500):

    a = random.randint(1,500)
    print(a)




# for문, while문 (while문은 잘 안씀)
# for는 목록에서 값을 하나씩 꺼내오는 것 

# for i in range(범위) : -> 함수 i에 범위(목록)에서 마지막 값까지 하나씩 값을 꺼내와서 저장
# 마지막 값을 꺼내오고 더 꺼내올 것이 없을때까지 값을 꺼내옴

# while -> 어떤 조건을 만족하기까지 반복 (True판정을 받는 동안~ )
# 조건을 한번 체크하고 어떤 조건에 부합이되면 while에 속한 것을 실행하는 것 
# 실행이 끝나면 다시 조건을 체크하고 실행하는 것
# 조건이 만족 되는 동안에 = while

