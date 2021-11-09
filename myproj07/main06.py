### format 사용해서 입력 업데이트!
# 최신기능은 계속 업데이트됨~ 이를 빠르게 파악해서 배우쟈

person = {
    "name": "Tom",
    "age": 10,
}

"{name} {age}".format(name=person["name"], age=person["age"])


"{name} {age}".format(**person)
"{name} {age}".format_map(person)

# 내가 학습할때 쓰던 버젼에만 한정되지 말기
# 내가 알고있는 거에만 국한 XX


"""
방탄소년단의 좋아요의 합은 ?

"""
import pandas as pd
from pprint import pprint
from collections import defaultdict, Counter

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


### 1

# List Comprehension with if statement
[
    song_dict["like"]
    for song_dict in song_list  # 원래 콜론을 쓰고 다음줄을 쓰는데 ?
    if song_dict["artist"] == "방탄소년단"
]

# for 앞으로 채워진것들~
# 밑줄의 if는? if문에 해당하는 것들만 append하겠다 라는 뜻

# 좋아요의 총합을 구하려면 ?
like_sum_for_bts = sum(
    [song_dict["like"] for song_dict in song_list if song_dict["artist"] == "방탄소년단"]
)

print(like_sum_for_bts)
