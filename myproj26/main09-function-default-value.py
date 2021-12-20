def get_defalut_value():
    print("get_defalut_value()를 호출")
    return 10




def hello(name,age=get_defalut_value()): # age변수는 디폴트값이 10으로 할당. 
    print(f"안녕. 나는 {name}이야. {age}살이지.")

hello("Tom")
hello("steve")
hello("john")




