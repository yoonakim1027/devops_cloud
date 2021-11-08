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
