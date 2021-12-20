number = 10

if number % 2 ==0:
    print("짝수")

else:
    print)"홀수"


for i in range(1,11):
    print(i)



for i in range(1,11,2):
    print(i) 
    # 1 이상 11미만의 간격에서 2씩 증가




## 함수 문법 

def mysum(x,y):
    return x+y

print(mysum(1,2))


mysum2 = lambda x,y: x + y

# 우항에서 새로운 함수를 만들고
# 함수를 mysum2라는 곳에 저장

#호출은?
print(mysum2(1,2))


def mysum5(x,y, *args):
    # 2개 이상의 인자를 받겠다.
    return x+y+sum(args)

print(mysum5(1,2,3,4,5))


