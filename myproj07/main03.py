"""
- 멜론 TOP100 리스트에서 
1. 좋아요 수가 가장 많은곡은? 가장 작은 곡은?
2. 곡명 단어 수가 가장 많은 곡은? 가장 적은 곡은?
3. 곡명 글자수가 가장 많은 곡은? 가장 작은 곡은?

"""


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

## 1. 좋아요 수가 가장 많은곡은? 가장 작은 곡은?
# song_list에서 최댓값을 찾겠다? ㄱ러면 리스트 안에있는 항목 하나를 반환
# 리스트 안에는 사전이 들어있다. 만약 여기서 최댓값/최솟값을 찾았다면? song_dict을 반환


# song_dict =max(song_list)
# print(song_dict) # 이렇게 실행하고자 하면, 실행이 안됨!


def peek_like_for_song(song_dict):
    return song_dict["like"]


song_dict = max(song_list, key=peek_like_for_song)  # 좋아요 수가 기준값이니까 이에 해당하는 함수를 만들어야 함!
print(song_dict)
# 이렇게 하면 출력이 됨! 근데 이거에 만족하면 안됨.
# 근데 song_dict이 비었을 때도 생각을 해줘야함.
# 에러는 100% 없앨 수 없음. 이를 잘 관리하는 것이 중요함
