# 2021.11.02

print("hello world")

#'9' >'19' -> 자리끼리 대소 비교 후 true/false 판단

# number = 10


import random
number = random.randint(1,100) #1이상 100이하

#import random -> 랜덤 디렉토리 설치 
# random.randint(몇이상, 몇이하) = 랜덤값


# ctrl + / => 드래그 범위 주석 처리  


# if number % 2 ==0 :
#     print("짝수입니다")

# if number % 2 != 0:
#     print("홀수입니다")


# else -> 앞선 조건이 거짓이라면 ~ 


if number %2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

# if를 쓰는 순간 하나의 그룹이 만들어지는 셈.
# else는 바로 위의 if만 신경쓰고, 각기 독립적으로 판단이 됨 ~ 
# if를 쓰는 순간 별개로 처리





