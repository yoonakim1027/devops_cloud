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


# (방법 1)
song_dict = max(song_list, key=peek_like_for_song)  # 좋아요 수가 기준값이니까 이에 해당하는 함수를 만들어야 함!
print(song_dict)
# 이렇게 하면 출력이 됨! 근데 이거에 만족하면 안됨.
# 근데 song_dict이 비었을 때도 생각을 해줘야함.
# 에러는 100% 없앨 수 없음. 이를 잘 관리하는 것이 중요함


##### song_list가 빈 리스트일 경우에 대한 대처
# (에러 처리 1번 대안)
song_dict = max(
    song_list, key=peek_like_for_song, default=None
)  # song_dict이 비었을 경우, None으로 처리해라
if song_dict == None:
    print("노래 목록이 비었습니다.")  # 이런식으로 에러가 발생했을때 대응하는 방법!
else:  # 아닐때는 ~ 그러니까 정상적일 때에는
    print(song_dict)


##### song_list가 빈 리스트일 경우에 대한 대처
#### 파이썬에서는 2번과 같은 방법을 많이씀~~~!!
# (에러 처리 2번 대안) default를 지정하지 X -> 근데 이렇게 하면 에러가 발생됨! 그러면 에러가 발생되게 그대로 두는 방법!
# try - except 사용
# 안에 있는 코드가 오류없이 실행되었을때? else 안에 있는 애들이 실행되는 것 !
# 오류가 발생되었을때 대응방법들!!
try:
    song_dict = max(song_list, key=peek_like_for_song)  # song_dict이 비었을 경우, None으로 처리해라
except ValueError:
    print("노래 목록이 비었습니다.")  # 이런식으로 에러가 발생했을때 대응하는 방법!
else:  # 아닐때는 ~ 그러니까 정상적일 때에는
    print(song_dict)


##### song_list가 빈 리스트일 경우에 대한 대처
# (에러 처리 3번 대안) 리스트가 판단 대상이 되어있을 때에는, 값이 비었을경우 False, 값이 있을경우 True
# 사고 치기 전에 사고가 날 것을 미리 정리!
if song_list:
    song_dict = max(song_list, key=peek_like_for_song)  # song_dict이 비었을 경우, None으로 처리해라
else:
    print("노래 목록이 비었습니다.")  # 이런식으로 에러가 발생했을때 대응하는 방법!
