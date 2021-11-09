#### 2021.11.09


# 지금의 풀이 :
# 1. 멜론TOP100 리스트에서 "곡명" 단어수로,  TOP10
# (1) 곡명 리스트를 만든 다음에
# (2) 출력(print) -> 이렇게 구분해서 설명하는 것이 좋음 !!
# ( 단어수가 제일 큰 노래가 우선순위가 가장 높겠죠 )


# - 출력(프린트), 데이터를 가공하는 것은 분리해서 생각하는 것이 좋음
# 데이터가공과 출력을 같이하려고 하지 말기!

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


### (1) 좋아요 수로 TOP10 곡명 리스트를 만들어보자
# 내림차순으로 정렬하고 처음 부터 10개를 출력하면 이게 TOP 10 !!!


# sorted(목록형 데이터, 키 이름 = 항상 지정해야함! 정렬 기준값을 지정해줘야함 -> 함수)
# song_list라는 사전을 참조하기 때문에,
def pick_like_value(song_dict):
    return song_dict["like"]


sorted(song_list, key=pick_like_value)
# sorted의 첫번째 인자로 항상 목록을 받음. 목록은 문자열, 집합 사전 다 됨!
####  sorted의 결과는 항상 리스트 !!!


### (1) sorted 오름차순 정렬
for song_dict in sorted(song_list, key=pick_like_value):
    print("{like} {title}".format(**song_dict))
    # 이렇게 출력하면 like가 가장 적은 곡부터 오름차순 정렬이 됨.


### (2) sorted 내림차순 정렬
for song_dict in sorted(song_list, key=pick_like_value, reverse=True):
    print("{like} {title}".format(**song_dict))


# sorted 자체는 새로운 리스트를 만들어준다!
# 이렇게 먼저 정렬. 코드는 가독성이 제일 중요함. 간결하다고 막 ~ 좋은 것은 아님
# 가독성이 좋아야 다른 팀원들이 코드를 받았을때 이해가 가능!

# sorted 방법 1
sorted_song_list = sorted(song_list, key=pick_like_value, reverse=True)
top10_song_list = sorted_song_list[:10]


# sorted 방법 2
for song_dict in sorted_song_list[:10]:
    print("{like} {title}".format(**song_dict))
