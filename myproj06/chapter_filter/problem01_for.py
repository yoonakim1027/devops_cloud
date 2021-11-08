from typing import List  # Type Hinting 기능 가져오기
import pandas as pd
from pprint import pprint

from main02 import get_title_for_song
df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 문제
# artist 글자수가 3글자 이상인 곡에 대해서 (필터링)
# 각 곡의 좋아요 수(합산 X)와 제목글자수의 곱을 출력해보세요. (변환)
# 1) for/if로 구현
# 2) filter/map 위주로 구현


# 각 곡의 좋아요 수는 그냥 출력
# 제목 글자수는 곱 

### for / if 사용해서 출력 

title_list = []
for song_dict in song_list:
    if len(song_dict["artist"]) >= 3:
        title_list.append(song_dict["like"]*len(song_dict["title"]))
        
pprint(f"각 곡의 좋아요와 제목글자수의 곱은 {title_list}")




## map / filter 사용 
# 1. artist 글자수가 3글자 이상인 곡에 대해서
# 2. 각 곡의 좋아요 수(합산 X)와 제목글자수의 곱을 출력해보세요.
# 각 곡의 좋아요 수는 그냥 출력
# 제목 글자수는 곱
# 필요한 정보만 map
def get_title_for_song(song_dict):
    return song_dict["title"], song_dict['like'], len(song_dict['title'])**2 

title_at_lease_3 = (list(map(get_title_for_song,song_list)))



pprint(title_at_lease_3)

title_list: List[str] = []

for song_dict in song_list:
    title: str = song_dict["title"]
    like: int = song_dict["like"]
    if len(title) >= 3:
        title_list.append(title)


### enumerate 사용법 
s = '안녕하세요.'

idx = 0
for ch in s:
    print(idx,ch)
    idx += 1

for idx, ch in enumerate(s):
    print(idx, ch)
# enumerate를 사용해서 손쉽게 사용 가능

# 시작값을 안주면 0부터 시작.
# 시작을 1부터 시작했으면?

for idx, ch in enumerat(s,1): # 시작값 1 
    print(idx, ch)


numbers = [
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,10],
]

# 대괄호여도 되고 소괄호 여도되는데 보통 소괄호 많이 씀
for idx, (x,y) in enumerate(numbers):
    print(x,y)

# enumerate 1씩 증가하는 일련번호를 얻고자 할때 사용하면 유용하다. 
# 소괄호
for x,y in numbers:
    print(x,y)


# 문제
# artist 글자수가 3글자 이상인 곡에 대해서 (필터링)
# 각 곡의 좋아요 수(합산 X)와 제목글자수의 곱을 출력해보세요. (변환)
# 1) for/if로 구현

from typing import List  # Type Hinting 기능 가져오기
import pandas as pd
from pprint import pprint

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

value_list: List[int] = [] # 리스트형식인데 int형식을 받겠다.
new_song_list: List[dict] =[]

for song_dict in song_list:
    artist:str = song_dict['artist']
    if len(artist) >= 3:
        value:int = song_dict['like'] *len(song_dict['title'])
        
        # 1번코드 
        new_song_list.append(dict(song_dict,value = value))

        # 2번코드 (1번이랑 2번이랑 같음)
        new_song_list.append({
            "title" : song_dict['title'],
            "artist" : song_dict['artist'],
            "like" :song_dict['like'],
            "album" :song_dict['album'],
            "rank" :song_dict['rank'],
            "value" : value,
# song_dict의 정보를 새로운 사전을 만들어서 list에 넣음
        }) # 그냥 정수를 append가 아니라, dict
# 리스트에 모아서 출력할 수도 있고, 그냥 프린트 할수도 있겠지

# 순차적이면 enumerate를 사용하면 되지만
# 지금 문제는 
# 곡명도 같이 출력하고 싶다면? 
for song_dict in new_song_list:
    print("{title} / {value".format(**song_dict))



# 2) filter/map 위주로 구현
