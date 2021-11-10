# 타이핑에만 집중하지 말고 ~
"""
2곡 이상 랭크된 가수는 몇 팀인가요?

"""

import pandas as pd
from pprint import pprint
from collections import defaultdict, Counter

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


### 1번 방법
# 몇 곡인지 알려면? 어떻게 해야할까 ?

# 어떤 가수가 몇곡의 노래가 올라가 있는지?
# 가수별로 올라가 있는 곡의 수
# 사전으로 표시하자면 {(키) 가수명 : (값) 올라가 있는 곡 수}

for song_dict in song_list:
    song_dict["artist"]
    # 아티스트가 몇번 나오는지만 중요함. 몇번이나 랭크업 되었나
    # 이거를 리스트로 바꾸려면?

## 리스트 컴프리헨션 버젼 (단순히 리스트)
artist_list = [song_dict["artist"] for song_dict in song_list]


# 이제 몇팀이나 되는지 보려면 ? counter를 쓸 수도 있음

# 먼저 직접 구현하는 방법 #
song_count_dict = {}  # key (아티스트) : value (song_count) # 가수가 몇곡이나 나왔는지
for artist in artist_list:  # 이 반복문은 100번 돌것임
    if artist not in song_count_dict:  # 사전에 등록되어(포함되어) 있지 않다면,
        song_count_dict[artist] = 0  # 초기화
    song_count_dict[artist] += 1
# 키에 등록되어있지 않으면~ (미리 등록되어있지 않은 사태를 미리 설정해서~)
# 출력을 이쁘게 보려면? pprint
pprint(song_count_dict)

### 2번 방법

# from collections import defaultdict

# 이 defaultdict(int 대신 여기에 dict을 넣어도 되고, list를 넣어도됨! )
song_count_dict = defaultdict(int)  # int 대신 0이라고 해주는게 아니라, 0이 시작점.
for artist in artist_list:  # 이 반복문은 100번 돌것임
    song_count_dict[artist] += 1

# 출력을 이쁘게 보려면? pprint
pprint(song_count_dict)


## defaultdict와 dict 의 차이는??
## KeyError가 발생할때, KeyError은 숨기고
# 지정된 디폴트 값으로 Key/Value를 저장한다.
# defaultdict 값이 0으로 저장되어있을 것.
## int()의 시작점은 0이다!!


###3번 방법
# 파이썬이 상황에 맞춰서 적절하게 사용할 수 있는 방법이 多
# from collections import defaultdict, Counter

song_count_dict = Counter(artist_list)
pprint(song_count_dict)


##### 1. 루프를 돌면서 1씩 증가~ (그런데 파이썬스럽지는 않음) : 나름 괜찮아요
## 값만 뽑아가지고, (키는 필요없음 )
## 곡수가 2개 이상인 팀은?
artist_count_avove_2 = 0
song_count_dict = Counter(artist_list)
for song_count in song_count_dict.values():  # .values() 값만 추출
    if song_count >= 2:
        artist_count_avove_2 += 1

print(artist_count_avove_2)

# 내가 핸들링하고 있는 데이터를 어떻게 뽑아내고?
# 어떻게 변환해야 하는지 적절하게 가공하는 것이 중요함


##### 2. 어떤 수를 받았을 때 2이상인지 체크
# filter/map 을 쓰는 방법이 무조건적으로 좋다는 것은 아님.
# for / if 랑 뭐가 더 나은지는 상황에 따라 적절히 구분
def check_above_1(song_count):
    return song_count > 1


# filter(함수, 무슨 값 ?)
# 가수별 곡수를 필터링
# filter는 len으로 셀 수 없음
# 리스트로 바꿔줘서 len !!
print(len(list(filter(check_above_1, song_count_dict.values()))))

# 코드가 눈으로 잘 모르겠으면 디버거 사용!
# 눈으로 잘 안보이면 노트에다가 변화를 그리기@@!!
# 한 번 봤는데 이해 다 되는 건 어려워~~!!
# 부단한 노력 ^__^

### format 방식 새로 업데이트 ^__^

person = {
    "name" : "Tom",
    "age" : 10,
}

"{name} {age}".format(
    name = person['name'],
    age = person['age'])
)

"{name} {age}".format(**person)
"{name} {age}".format_map(person)