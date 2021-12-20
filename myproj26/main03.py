tom = {
    "name" : "Tom",
    "age" : 10,
    "ag" + "e": 10,
    age : 10,
}


#  2.
# 파이썬에서는 그냥 tom1
name = "Tom"
age = 10
tom1 = {
    "name" : name, #name이라는 변수 값 참조
    "age" : age, # age라는 변수값 참조

}

# 파이썬은 눈에 보이는 데로, 이게 전부임 


# f스트링 문법 : String Interpolation
print(f"안녕 나는 {name}이야 ")

