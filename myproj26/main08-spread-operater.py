#name, *rest = ['tom',10,'seoul']

# 각각의 값을 인덱스로서 구분
# name에는 Tom이 저장
# 나머지 값들은 뭉쳐서 rest에 저장


numbers = [1,2.3]
new_numbers = [
    10,20,30,
    *numbers,
    40,50,60,
    *numbers,
    70, 80,90,
    *numbers,

]
# *을 붙이면? 한개의 변수에 담긴 값을 펼치는 것
# unpack

print(new_numbers)


tom = {
    "name":"Tom",
    "age" : 10,
    "region" : "seoul",
}
# tom과 steve는 이름만 다르고 다른 값이 같을때?
# 이름만 바꾸고 싶다면 ?
# age, region이 같다면?
# tom을 참조하여 name만 변경해서 
# 새로운 steve를 만들고자 함
steve= dict(tom, name="steve")
# name이라는 키 밸류만 새로 지정 

print(steve)