
## 최댓값 구하기 
## 최댓값 구하는 함수 정의하기 
# ## 어떤 구현을 할 때마다 함수 정의! 

# def get_max_number(number_list):
#     #최댓값을 저장할 변수가 필요함
#     return 0 # 아직 구현을 안한 상태! 


# numbers = [17, 92, 18, 33, 58, 7, 33, 42]

# print(get_max_number(numbers)) # 92가 나오겠지 ?

# # 근데 이렇게 실행하면 결과값이 0이 나옴! 


## 그렇다면 이렇게 바꾸면 ? 
def get_max_number1(number_list):
    number = number_list[0] # 인덱스 하나씩 꺼내와서 큰값을 number에 저장하게 됨 
    for current_number in number_list: 
        if current_number > number :
            number = current_number

    return number # 다돌고나면 최댓값이 number에 남게됨 


numbers = [17, 92, 18, 33, 58, 7, 33, 42]
print(get_max_number1(numbers))

# 이렇게 바꾸면 최댓값이 나옴 



### 최댓값의 인덱스 출력하기 1(수동)  

def get_max_index(number_list):
    number = number_list[0] # 인덱스 하나씩 꺼내와서 큰값을 number에 저장하게 됨 
    index = 0
    max_index = 0
    for current_number in number_list: 
        if current_number > number :
            number = current_number #최댓값을 저장하는 과정
            # 추가로 인덱스를 저장하는 과정이 필요함
            # 처음 가져온 값은 인덱스가 0
            max_index = index
            index +=1 #매 순회 돌때마다 1씩 증가  
        # 인덱스 값은 매번 바뀜     

    return max_index # 다돌고나면 최댓값이 number에 남게됨 




### 2 수동으로 index변수를 만들지 않고 자체적으로 만드는 방법

def get_max_index1(number_list):
    number = number_list[0] # 인덱스 하나씩 꺼내와서 큰값을 number에 저장하게 됨 
    max_index = 0
    for index, current_number in enumerate(number_list):
        # 파이썬을 쓴다면, 인덱스를 순차적으로 증가시켜야할때 
        # 수동으로 증가시키는 코드는 잘 사용하지 않음.
        # enumerate를 사용해서 값을 자동으로 생성할 수 있음. 
        if current_number > number :
            number = current_number #최댓값을 저장하는 과정
            # 추가로 인덱스를 저장하는 과정이 필요함
            # 처음 가져온 값은 인덱스가 0
            max_index = index
            index +=1 #매 순회 돌때마다 1씩 증가  
        # 인덱스 값은 매번 바뀜     
    return max_index # 다돌고나면 최댓값이 number에 남게됨 


numbers = [17, 92, 18, 33, 58, 7, 33, 42]
print(get_max_index1(numbers))


## 최댓값을 구해주는 파이썬에서 제공해주는 것 3 

# 문자열에도 인덱스가 지정이 됨. 문자열은 문자들의 모음 
