def get_defalut_value():
    print("get_defalut_value()를 호출")
    return 10



# 파이썬은 함수 정의 시점에 호출이 된다 ! 

def hello(name,age=get_defalut_value()): # age변수는 디폴트값이 10으로 할당. 
    print(f"안녕. 나는 {name}이야. {age}살이지.")

hello("Tom")
hello("steve")
hello("john")



# 자바 스크립트에서는? 디폴트 값이 필요 할때만 호출
# 파이썬에서는? 함수가 만들어질 때 디폴트 값이 호출

# 그러면, 파이썬에서 디폴트 값이 필요할 때마다 그 함수가 호출이 되게 하려면 ?

# 자바 스크립트와 파이썬은 비슷해보이지만, 구현방법이 조금씩 다르다.
def hello(name, age=None): # 이함수가 호출될때마다 호출! 
    if age is None:
        age = get_defalut_value() # 그러니까 이 로직을 함수 안에다 넣어줌  
    print(f"안녕. 나는 {name}이야. {age}살이지.")


# age는 None으로 지정하면? 인자가 없으면 none



