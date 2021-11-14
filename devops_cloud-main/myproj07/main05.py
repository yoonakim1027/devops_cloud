"""
2곡 이상 랭크된 가수는 몇 팀인가요?
"""

from collections import defaultdict, Counter
from pprint import pprint
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

artist_list = [song_dict["artist"] for song_dict in song_list]

# 1
# song_count_dict = {}  # key: artist, value: song count
# for artist in artist_list:
#     if artist not in song_count_dict:
#         song_count_dict[artist] = 0
#     song_count_dict[artist] += 1

# 2
# KeyError가 발생할 때, KeyError를 숨기고
# 지정된 디폴트 값으로 key/value을 저장합니다.
# song_count_dict = defaultdict(int)  # key: artist, value: song count
# for artist in artist_list:
#     song_count_dict[artist] += 1

# 3
song_count_dict = Counter(artist_list)

# 1 : 나름 괜찮아요.
artist_count_above_2 = 0
for song_count in song_count_dict.values():
    if song_count >= 2:
        artist_count_above_2 += 1
print(artist_count_above_2)

# 2
def check_above_1(song_count):
    return song_count > 1


print(len(list(filter(check_above_1, song_count_dict.values()))))
