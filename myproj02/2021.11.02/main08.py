def calculate_sum(max_number):
    # 1부터 시작해서 max_number 까지의 합을 구하기
    accumulator = 0 # 값을 누적할 변수 
    for i in range(1,max_number + 1): # 1부터 시작해서 max_number+1까지 순회 
        accumulator += i
    return accumulator
    
#     # 이 값이 i로 하나씩 들어가게 되는 것 -> 누적


print(calculate_sum(100))



import turtle as t
def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)


def polygon2(n,a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)

polygon(3)
polygon(5)

t.up()
t.forward(100)
t.down()



#eval함수는 절대 사용하지 않음

