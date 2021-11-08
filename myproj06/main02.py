import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

"""
멜론TOP100 리스트에서 "곡명" 단어수 출력
총 100줄 중에 한 줄 출력 의 예 : Dynamite ➡ 1
"""

"""
멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력
단어수가 제일 큰 노래가 우선순위가 가장 높겠죠.
"""

#### 9

# 곡명의 단어수로 구성된 리스트를 만들어 보자

# 멜론 "곡명 / 단어수" 리스트 만들기


# 의미있는 이름 짓기가 중요함 !

#
for song_dict in song_list:
    title: str = song_dict["title"]
    # 순수하게 곡명 단어수를 출력하려면 ?
    title_length = len(title)  # 목록성향을 가진 title의 갯수를 알려줌. 딕셔너리든 리스트든 가능
    print(title, title_length)


# map -> 값을 변환

# 사전이 온다면?
def get_title_for_song(song_dict):
    return song_dict["title"]  # get_title_for_song 함수를 써서, 한곡에대한 정보를 통해 제목만 리턴


# filter는 변환이 아님
for song_dict in song_list:
    # 변환을 담당하는 함수
    print(get_title_for_song(song_dict))

title_list = list(map(get_title_for_song, song_list))
print(title_list)

#for song_dict in filter(함수,song_list):

for title in map(get_title_for_song, song_list):
    print(f"{title} - {len(title)}) # 순회를 돌면서 100곡에 대한 출력


# 새로운 함수 생성
def get_title_and_length_for_song(song_dict):
    title: str = song_dict["title"]
    return [title, len(title)]
    # 제목이 있으면, 여기에 리스트로 타이틀과 len(title)을 리턴
    # 리스트라는 자료구조, 튜플, 사전 이라는 자료 구조를 리턴할 수 있음
    # 리스트도 값이 한개, 사전이 값이 한개 -> 이 한 개를 리턴하지만 여러개를 리턴 하는 효과가 있는 것.

# 리스트가 두개 항목을 리턴하기 때문에,  for문에서도 두개로 인자 갯수를 맞추는 것


for title, length in map(get_title_and_length_for_song, song_list):
    print(title, length)