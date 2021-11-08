# README는 무조건 대문자 // 확장자는 소문자 

# 내장함수 filter

# md는 마크다운의 약자 ! 



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

# 실습하는데에 README 파일만들어서 코드 메모~ 