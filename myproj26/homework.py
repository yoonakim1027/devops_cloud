import random
numbers = [1, 2, 3, 4, 5]

new_numbers = []
for number in numbers:
    new_numbers.append(number ** 2)


new_numbers2 = [
    number ** 2 for number in numbers
]


# 내장함수 map
def mapper(number):
    return number ** 2


print(list(map(mapper, numbers)))

print(list(map(
    lambda number
    number ** 2,
    numbers,
)))


numbers2 = [1, 3, 4, 5, 2]
# 1) 내장함수 sorted
print(sorted(numbers2))
# 기본은 오름차순 정렬
print(sorted(numbers2, reverse=True))  # 기본이 False.
# 이렇게 하면 내림차순


numbers3 = [31, 89, 24, 81, 46]
# 다양한 기준으로 정렬할 수 있음!


def make_value(number):
    return number % 10


print(sorted(numbers3, key=make_value))
# numbers3의 갯수만큼 make_value함수가 호출됨
# 정렬 기준값이 key= 함수


# 2) 리스트의 sort
numbers3.sort()
numbers3.sort(key=make_value)
numbers3.sort(key=lambda number: number % 10)
print(numbers3)


# 호출할 때마다 랜덤수가 출력
def make_random_value(number):
    return random.randint(1, 100)


numbers3.sort(key=make_random_value)
print("random  values:", numbers3)
