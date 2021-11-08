# #타자 게임

# names = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]

# # 자료구조 list
# # range(1,5) -> 1,2,3,4의 목록이 만들어짐
# # for i in range(1,5):
# #   print(i) -> 이거는 리스트 형식이 아님

# # 리스트는 [] 대괄호를 사용
# # for i in [1,2,3,4]:
# #     print(i)

# # # 미리 리스트를 생성하는 것보다 그때그때 동적으로 생성하는 것이 유연한 방식
# # # 우리가 타이핑할 문자열의 목록 ->


# # import random
# # random.choice(range(1,10))
# # random.choice([1,2,3,4,5,6,7,8,9])
# # random.choice(names)


# # time.time() -> 시간 기록해주는 함수


# import random
# import time

# start = time.time()
# q = random.choice(names)


# animal_names = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]


# # 총 횟수 = 5회만 줌

# input("준비되셨으면, 엔터키를 입력해주세요 ")

# begin_time = time.time()
# ok_counter = 0
# for count in range(5): # 총 5회 실행
#     random_name = random.choice(animal_names)
#     print(random_name)
#     line = input(">>>")
#     # 총 5회 실행, 그중에서 랜덤으로 뽑았고,
#     if random_name == line: #같으면 맟추고, 다 되면 틀린 것
#         ok_counter += 1
#         print("정확합니다")
#     else:
#         print("오타가 있습니다")


#          # 그러나 이렇게 되면 중복된 문제가 들어올 수 있음!


#### 타자수를 알려주는 프로그램을 만들자 (과제)
# 성공하면? 당신은 분당 어느정도다~라고 알려주기

import random
import time

animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]

input("준비되셨으면, 엔터키를 입력해주세요.")

begin_time = time.time()

ok_counter = 0

### 중복값 있게 그냥
for count in range(5):
    random_name = random.choice(animal_names)
    ## 방법1 : 이미 사용된 random_name을 받았다면 다시 가져오는 것 ?
    print(random_name)
    line = input(">>> ")
    if random_name == line:
        ok_counter += 1
        print("정확합니다.")
    else:
        print("오타가 있어요.")

end_time = time.time()

print(f"{ok_counter}번 성공하셨습니다.")
print(f"총 {end_time - begin_time}초가 걸리셨어요.")


## random.sample() 중복없이 원하는 수만큼 사용 가능

## 중복하지 않고는 ?

# random.shuffle()

animal_names1 = random.shuffle(animal_names)  # animal_names안에 있는 인덱스를 섞어버림
# print(animal_names1)


# 슬라이싱은 대괄호 사용
print(animal_names[0:5])  # 0이상 5미만

## 인덱스
## 목록을 대괄호로 표시하는데, 목록에 첫번째는 0부터 시작함
## 목록의 첫번째 값을 읽어오고 싶을때, 대상을 지


#### 중복되는 값 없이 하면?
begin_time = time.time()

ok_counter = 0

for random_name in animal_names[0:5]:
    # 인덱스를 뽑아서 지정한 것들 사이에서 빼내오는 거라 중복값이 없음!!!!!
    print(random_name)
    line = input(">>> ")
    if random_name == line:
        ok_counter += 1
        print("정확합니다.")
    else:
        print("오타가 있어요.")

end_time = time.time()
time_cu = end_time - begin_time
time_cu = float(format(time_cu, ".2f"))

# cul_time = time_cu/60

print(f"{ok_counter}번 성공하셨습니다.")
print(f"총 {time_cu}초가 걸리셨어요.")

# print(f"분당 {cul_time}")


# 분당 타이핑 속도를 알려주도록 개선 -> 몇분당 몇 타이핑....?

# 타이핑 속도는 분당 몇타이십니다
# 몇타인지 계산하려면? 맞추는데 몇타를 쳤다.. ?
# 글자수로도 몇타를 계산할 수 있음.
#
# 분당 타이핑 속도계산하려면?
# 분당 몇개나 쳤나 확인
