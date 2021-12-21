def base_10(fn): # base_10함수가 호출이 되면 
    def wrap(x,y): # 매번 새로운 wrap라는 함수를 만들어서 리턴
        return fn(x,y) +10
    return wrap
# 이렇게 함수를 인자로 받고, 
# 내부적으로 함수를 만들어서 리턴할 수 있음 
# 이렇게 하는 것이 파이썬의 장식자
# Decorators 

# 1 번
@base_10 
@base_10 # 이렇게 두번 할 수도 있음 -> 그러면 20이 깔림 
def mysum(x,y):
    return x+y

# 2번 (1번, 2번은 같은 것! )
mysum = base_10(base_10(mysum))
print(mysum(1,2))

# 이렇게 동일 함수로 두번 감아쓸 수 있음



