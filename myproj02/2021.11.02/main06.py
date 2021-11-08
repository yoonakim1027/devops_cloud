# 구구단

def gugudan(number): # 함수정의
    print(f"### {number}단 ###")
    for i in range(1,10):
        print(f"{number} * {i} = {number*i}")
# 영역지정하고 tab
# shift tab 하면 들여쓰기 빠져나옴


# 함수 호출 부분을 for 반복문으로 변경해보세요.

for j in range(1,10):
    gugudan(j) #함수호출

for number in range(2,10):
    gugudan(number)



####  함수의 구성요소
# 함수의 이름 : 1개
# 함수의 인자 (Arguments) : 0개 이상
# 함수의 반환값 (Return value) : 1개

# 함수 호출 시 얻는 값 -> 반환값  = 반환한다
