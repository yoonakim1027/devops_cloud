# 기초 데이터로서 멜론 top100 리스트 구성하기

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list

# 과제 1
# 방탄소년단의 곡명만 출력해보세요
# 방탄소년단은 'artist' 칼럼에 속해있음
df.info()

for song in song_list:
    if song["artist"] == "방탄소년단":
        print(song["title"])

# 과제 2
# 곡명에 "가을"이 들어가는 곡명만 출력해보세요
for name in song_list:
    if "가을" in name["title"]:
        print(name["title"])

# 과제 3
# 좋아요 수가 200000이 넘는 곡수는?
like_count = 0
for like in song_list:
    if like["like"] > 200000:
        like_count += 1
print(like_count)

# 과제 4
# 가수 별 곡 수를 출력해보세요

# 1. 필요한 정보 추출 (가수 목록)

artist_split = []  # 빈 리스트 생성
for song in song_list:
    artist_split.append(song["artist"])

singer = set(artist_split)

print(len(singer))

dict_total = {}  # 새로운 딕셔너리 생성
for name in singer:  # 중복제거한 값
    count = 0
    for i in artist_split:
        if name == i:
            count += 1
            dict_total[name] = count
    print(f"{name} :  {count}곡")



### 2
# 가수 별 곡수를 출력하기 

artist_dict ={}

for song_dict in song_list:
    artist: str = song_dict['artist'] #아티스트만 모아서 출력하면 됨 
        # 타입 힌트 -> 명시적으로 타입을 지정해줌. 그러면 좀 더 코딩할 때 덜 헷갈리고 가능 
    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1
    
    # 곡수를 매번 1씩 증가시켜주면 됨 .
    
    #artist_list.appned(artist)
print(artist_dict)

# {
#     "방탄소년단":"값",
# }

# artist_dict["방탄소년단"] = 0 
# artist_dict["방탄소년단"] = artist_dict["방탄소년단"]  +1 



