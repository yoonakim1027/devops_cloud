"""
"방탄소년단" 곡명만 출력하기
곡명에 "사랑"이 포함된 곡명만 출력하기
"좋아요" 수가 200,000 이상인 곡명만 출력하기
"""

from typing import List  # Type Hinting 기능 가져오기
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 방탄소년단의 곡명 문자열로 구성된 리스트를 만들어 보세요 .
# 데이터를 먼저 만들어 두고 출력하는 것 .

for song_dict in song_list:
    song_dict["title"]
# 여기서 단순히 print를 할 수도 있고,
# 여기에 우리가 title_list라는 새로운 리스트를 만들어서 여기에 append할 수도 있음.

title_list = []
for song_dict in song_list:
    title_list.append(song_dict["title"])

# 리스트면 [인덱스]
# 인덱스 범위를 벗어난 인덱스 범위를 지정하면 인덱스 에러
# 잘못된 키(딕셔너리)면 -> 키에러  KeyError

# title_list는 문자열인데, 문자열로만 구성할 거다!
title_list: List[str] = []  # 사실 이거는 없어도 동작하는데,
# 코드의 가독성을 높이거나
# 코드의 품질을 높이기 위해서
# 파이썬을 더 선도적으로..잘쓰고자 하는 회사들이 이렇게 타입을 지정함.

for song_dict in song_list:
    # 제목의 경우도 별도의 변수로 할 수 있음
    artist: str = song_dict["artist"]

    if artist == "방탄소년단":  # 이 조건에 부합하면?
        # 들여쓰기 하려면? 콜론 쓰면돼!
        title: str = song_dict["title"]
        title_list.append(title)  # 위에서 title이라는 str만 넣을 변수를 새로 만들어서 여기에 append 하겠다.
    # 중간에 print 하지말고 밖에 print 하는 걸 위주로 해야함.
print(title_list)  # 이렇게 !

# 코드는 최대한 정제해서 깔끔하게 쓰려고 노력해야함.
# 단순히 동작만 하는 것에 만족하면 안됨. 좀 더 좋은 코드를 쓰기위해 고민하고 노력이 필요


#### 2 
# print보다 데이터를 만드는 데에 집중!
# 곡명에 "사랑"이 포함된 곡들의 곡명 리스트를 만들어보세요! 

# 참조할 것은? 곡명 (title)
for song_dict in song_list:
    title: str = song_dict["title"] # title로 접근해서 문자열로 곡명만 가져옴 (이 리스트는 100번 돌거임)
    # 곡명의 타입은? 문자열의 성격
    # 사랑이 포함된 곡들?
    if "사랑" in title: # in의 뒤에 올것은? 목록의 성격을 가진 것들. 리스트, 집합, 사전 같은 목록의 성격을 가진 값들이 in 뒤에옴
    # 앞에 있는 값이, 뒤에 있는 값에 포함이 되느냐?
    # 결과는 ? True /False 
        title # print로 하는 것 보다, 데이터를 반환하는 것을 쓰셈! 
        # 지금은 title만 썼기 때문에 값이 출력되지도, 아무런 동작을 하지도 않음! 

title_list : List[str] = []

for song_dict in song_list:
    title: str = song_dict["title"]
    if "사랑" in title: # 우리가 판단 기준에 의거, 판단 기준에 부합되었을 때에만 코드를 실행! 
        title_list.append(title) # 조건에 부합했을 때에만 append로 title을 title_list로 추가하겠다.



#### 3
# 좋아요 수가 20만 이상인 곡명의 리스트를 만들어보세요.

# 출력은 데이터를 다 만들고 데이터를 출력하거나 엑셀로 보내거나 .. 활용이 다름
# 데이터를 처리하는 과정 / 데이터를 print하는 과정을 분리해서 따로 생각해야 함 

# song_list에서 여러 곡들을 순회해야지만 해결 할 수 있는 문제! 
# 필요한 자료? 좋아요수(like) / 곡명(title)

title_list: List[str] = [] # title_list는 문자열로 구성된 데이터이다 ! 
for song_dict in song_list:
    title: str  = song_dict['title'] # 이렇게 별도의 변수에 담아서 처리하는 것이 이해하기 더 쉬움
    # 이렇게 접근하는 속성이 서너개가 쌓이면, 보기 힘들어서 이렇게 개별로 끊어서 나눠서 생각하는것이 이해하기 쉬움
    like: int  = song_dict['like']
    # title이라는 변수를, 어떤 기준에 의해 
    if like >= 200_000: # 정수는 언더바 써서 나눠도 똑같음~ 
        # 위에서 만든 title_list에 해당하는 값만 append
        title_list.append(title) # 문자열만 추가한 것 
        
print(title_list)

# filter를 사용하지 않고 for와 if 만으로 푼 문제 


#### 4 


"""
"방탄소년단"의 곡명 문자열로 구성된 리스트를 만들어보세요.
"""


new_song_list : List[dict] = [] #사전인데 dict가 들어갈거야. 리스트에는 무엇이든 들어갈 수 있음! 
for song_dict in song_list: # 원본 데이터는 song_dict 
    artist: str = song_dict["artist"]
    if artist == "방탄소년단":
        new_song_list.appned(song_dict) # song_dict : 현재의 곡 정보 (type : 사전)
        # 전체 곡정보를 다 넣은 것!! 
        # 파이썬의 장점 : 리스트의 자료구조 / 사전의 자료구조가 정말 강력하고 유연함! 
        # 정말 효율적으로 데이터를 처리할 수 있음.

print(title_list)


##### 5 


from ppring import pprint  
"""
"방탄소년단"의 곡명 문자열로 구성된 리스트를 만들어보세요.
"""

new_song_list : List[dict] = [] #사전인데 dict가 들어갈거야. 리스트에는 무엇이든 들어갈 수 있음! 
for song_dict in song_list: # 원본 데이터는 song_dict 
    artist: str = song_dict["artist"]
    if artist == "방탄소년단":
        new_song_list.appned(song_dict)

# from pprint import pprint 
pprint(new_song_list) # pprint  좀 더 이쁘게 보여주는 프린트! 


# 대괄호로 시작했다는 것은 리스트로 시작했다는 것
# 중괄호로 시작했다는 것은 딕셔러니 


##### 6

## filter : 어떤 조건에 부합하느냐 아니냐! 
# 조건에 부합 : 통과 // 조건에 부합하지 않음 : 안돼 ! 

# 함수라는 것은 여러줄의 코드를 함수라는 이름으로 묶어두는 것
# 함수에 속한 코드를 실행하려면? 함수이름만 데려오면 실행이 됨 ! 
# 내가 설계하는 것이라 어떻게든 만들 수 있음


## 1. 로직을 구별해주는 함수를 만들기 
    # bts의 노래라면 True를 리턴
    # 아니라면, False를 리턴할 것.
    ####  이 함수에게 기대하는 것은? True /False를 리턴하는 것 ! 
def check_bts_song(song_dict):
    """
    BTS 노래라면 True를 반환합니다. # 함수를 시작하자마자 써야함!! 그러면 한글로 설명이 나온당 
    """
    artist : str = song_dict['artist'] # artist에는 매 곡의 아티스트들만 출력!
    return artist == "방탄소년단" # == 비교 연산자 -> 값이 같냐 아니냐 ? 같으면 True / 다르면 False 
# 한 곡에 대한 정보를 기대하는 것. 기대하는데 ? 값을 안주면 ? 코드 실행중에 에러가 날 것 
# 지금 보면 dict라는 사전형식으로 받기 때문에, 다른 타입을 넘겨주게 되면 오류가 남


new_song_list : List[dict] = [] #사전인데 dict가 들어갈거야. 리스트에는 무엇이든 들어갈 수 있음! 
for song_dict in song_list: # 원본 데이터는 song_dict 
    if check_bts_song(song_dict): # 함수명을 쓰고 소괄호를 열고 닫으면 -> 함수를 호출한다(call)
    # 수행이 끝나면 return값을 갖게 됨.
    # 참을 리턴 : bts의 노래구나 ~
    # 거짓을 리턴 : bts의 노래가 아니구나~
pprint(new_song_list)

# for 안에 직접 bts노래인지 아닌지 로직을 for안에 넣어서 하는 것과
# 별도의 함수를 사용해서 체크하는 것은 구동은 똑같지만 
# 조금 더 코드를 읽는데에 도움이 되는 것은? def 함수를 사용해서 코드를 줄이는것!
# 함수를 쓰는 이유 : 어떤 일련의 코드를 나열 -> 한번에 이해가 안될 수 있음
# 코드를 한 데 묶어서 의미있는 이름을 지어서 하면? 좀 더 의미파악이 쉽게 됨 

# 함수를 쓸때? 
# """ """ 쌍따옴표를 써서 안에 한글을 쓰면 설명도 나옴 ! !! 



#### 7

# filter의 첫번째 인자 : 함수 
# filter로 통과 시킬것인지 아닐것인지 결정하는 함수 ! 

new_song_list = list(filter(check_bts_song, song_list))

# 단순히 print로만 한다고 하면?
for song_dict in filter(check_bts_song, song_list):
    print(song_dict) # 단순히 print만 한다면 리스트로 안바꿔도 for를 사용해서 루프돌 수 있음

# for / if로만 해도 지장은 없지만, 데이터가 많아질 경우 filter를 사용해서 처리할 수 있어야 효율적으로 처리할 수 있음

for song_dict in filter(check_bts_song, song_list):
    print("{title} {artist} {like}".format(**song_dict))
    # .format(**리스트 이름)

## 곡명에 사랑이 포함된 곡들의 곡명 리스트 

# song_list는 한 곡에 대한 정보가 사전으로 되어있고, 100개
def check_contains_love(song_dict): # song_list는 한 곡에 대한 정보가 사전으로 되어있고, 100개
    title: str = song_dict['title'] # 여기가 왜 song_dict를 받는지..? 질문 
    return "사랑" in title

    # 한 곡에 대한 정보를 받았을때, 제목만 참조해서 제목에 사랑이 포함되어있으면 True / 아니면 False

for song_dict in filter(check_contains_love, song_list): 
# 곡명에 사랑이 들어간 것들이 필터 되서~ 사전만으로 for 반복문이 돌게 된다.
    print("{title}".format(**song_dict)) 
    # 여기가 왜 

#### rank

##### 8 
# 좋아요 수가 20만 이상인 곡들의 곡명 리스트

def check_above_200000(song_dict):
    like : int = song_dict['like']
    return like >= 200000 # 한곡에 대한 정보만 받아서 like가 20만이 넘는지 아닌지만 보여줌

for song_dict in filter(check_above_2000000, song_list):
    print("{title} - {like}".format(**song_dict))

# 어떻게 filter할 것인지는 별도의 함수에서 정하는 것임 ! 



