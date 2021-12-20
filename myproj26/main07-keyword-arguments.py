# 키워드 인자활용문법

def mysum3(x,y,z):
    return x+y*10+y +z*100

# 위치 인자: 각각의 순서를 구분하는 방법은 인덱스 
print(mysum3(1,2,3))

# 키워드 인자 : 이름을 지정해서 넘김. 순서가 바뀌어도 상관없음
# 각각의 이름을 구분하는 것은 이름임 
print(mysum3(x=1,y=2,z=3))
print(mysum3(y=1,x=2,z=3))
# 키=값 
kwargs = {"x":1, "y":2, "z":3}

# 한개 변수에 담겨 있는 값을 풀어서 여러개의 인자인 것 처럼 넘김
# 이는 언패킹이라고 함 
mysum3(**kwargs)
# unpacking


# people라는 리스트 (순회)
people = [
  { "name": 'Tom', "age": 10, "region": 'Seoul' },
  { "name": 'Steve', "age": 12, "region": 'Pusan' }
]

# 참조하는 대상이 people이라는 리스트.
# 이 people리스트 안의 값을 하나씩 순회를 돔
for person in people:
    print(person)

# 출력을 name과 age만 하고싶다면?
for person in people:
    print(person['name'],person['age'])

