mylist = [
    1,
    2,
    3,
    4,
    5,
]

for number in mylist:
    print(number)

# 이렇게 하면 5개가 출력이 됨
mylist = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
]

for number in mylist:
    print(number)
    # 이렇게 해도 5번 돔!

x,y = 1, 2 # x에는 1이 대입, y에는 2가 대입. 우항 좌항의 갯수는 동일해야함
#  x,y = 1 

mylist = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
]

for x,y in mylist:
    print(x,y)

# 파이썬의 for 특징
# 값을 하나 받아서 for의 변수에 대입하고 수행하고 수행이 끝나면 두번째것을 수행... 
# 값을 가져올 것이 없을 때까지 수행 ! 


# 갯수를 맞춰줘야함


### 방탄소년단의 노래에 대해서만, 곡명과 곡명의 글자수를 출력
# 1. 방탄소년단의 노래만 filter를 통해서 필터링. 
# 2. 필터링된 결과를 map을 통해 변환

bts_list = []
for song_dict in song_list:
    if song_dict['artist'] =='방탄소년단':
        title: str = song_dict['title']
        bts_list.append([title, len(title)]) # 이제 이거에 대한 리스트를 만든 것이 bts_list = []
        # 제목과 글자수로 구성된 리스트를 bts_list에 담는 것

for title,length in bts_list:
    print(title, length) # 이렇게 두 개의 인자만 출력할 수 있음.


##### 10 filter / map 버전

def check_bts_song(song_dict):
    return song_dict['artist'] == '방탄소년단'

# map(변환하는 함수, 변환할 대상(목록 : 사전, 문자열 등등.. ))
filter(check_bts_song,song_list)

for title, lenght in map(
    get_title_and_length_for_song,
    filter(check_bts_song,song_list)
    ) # 이 자체가 목록을 반환함! 
    print(title, length)



## 문제 
# artist 글자수가 3글자 이상인 곡에 대해서 
# 첫번째 조건 : filter 어떤 조건에 부합하는지 ?

# 좋아요 수와 제목 글자수의 곱을 출력해보세요. 
# 두번째 조건 

# 1 번 : for / if로 구현하기
# 2 번 : filter/ map 위주로 구현 

# 문제
# artist 글자수가 3글자 이상인 곡에 대해서
# 각 곡의 좋아요 수(합산 X)와 제목글자수의 곱을 출력해보세요.
# 1) for/if로 구현
# 2) filter/map 위주로 구현

tile_list = []
for song_dict in song_list:
    if len(song_dict['artist']) >= 3:
        title: str = song_dict['title']
        bts_list.append([title, len(title)]) 