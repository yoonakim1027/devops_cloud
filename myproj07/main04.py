import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

""" 리스트에 랭크된 가수는 총 몇 팀인가요? 
(중복 제거한 가수명 리스트의 크기)
100개의 대한 리스트
1개씩 사전으로 저장


"""

## 1번 방법 for

artist_list = []
for song_dict in song_list:  # song_dict의 ['artist']만 필요한 상황!
    artist: str = song_dict["artist"]
    artist_list.appned(artist)
    # 근데 이렇게 하면 중복이 존재함. 리스트는 중복을 알아서 제거하지 않음
    # append한 만큼 붙힘
    # 이렇게 쓰면? artist_list에는 총 100개의 문자열로 구성된 아티스트이름이 리스트업 되어있음


# 중복제거 로직 직접 구현
# 아티스트 리스트에 추가되어있지 않으면 append
artist_list = []
for song_dict in song_list:  # song_dict의 ['artist']만 필요한 상황!
    artist: str = song_dict["artist"]
    if artist not in artist_list:
        artist_list.appned(artist)

artist_list


## 2번 방법

# 똑같이 순회돌기
# 중복 배제의 목적 - > 중복제거해주는 set
artist_set = set()  # set쓰고 소괄호 쓰면 빈 집합이 만들어짐
for song_dict in song_list:
    artist: str = song_dict["artist"]
    artist_set.add(artist)
    # 집합은 순서의 개념이 없기때문에, 추가하고싶으면 add()
    # 리스트는 순서의 개념이 있어서 append(), insert()

print(len(artist_set))

# 리스트를 써서 구현하는 방법 / 집합(알아서 중복제거 가능)을 사용해서 구현하는 방법
# 해당하는 값들로 구성된 리스트 / 집합

## 3번째 방법 : 리스트 컴프리헨션
artist_set = set([song_dict["artist"] for song_dict in song_list])

print(len(artist_set))
# 리스트를 먼저 만든다음에 집합으로 변환하는 방식


## 4번 방식 : Set Comprehension
# 시작부터 리스트를 만들고 집합으로 변환하는 것이 아니라,
# 만들어질 때부터 집합인 것.


artist_set = {song_dict["artist"] for song_dict in song_list}

print(len(artist_set))
