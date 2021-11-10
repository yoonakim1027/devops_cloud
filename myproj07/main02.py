### (1) 좋아요 수로 TOP10 곡명 리스트를 만들어보자
# 내림차순으로 정렬하고 처음 부터 10개를 출력하면 이게 TOP 10 !!!
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
# 각 곡명에 대한 단어 갯수
def pick_word_count_for_title(song_dict):
    title: str = song_dict["title"]
    word_list = title.split()  # 문자열로 구성된 문자열 리스트 생성됨
    # 여기서 word_list의 갯수가 중요하다면?
    return len(word_list)  # 정렬 기준값만 바뀐 것!

    # wordcount ! 순수하게 정렬할때만, 정렬 기준값으로만 사용했기 때문에
    # 정렬을 위해 참고할 목적으로만 잠깐 쓰려고 한거

    # map을 통해 정렬기준값이 포함된 사전을 생성
    # -> 정렬기준값을 먼저 한다음에 sorted


sorted_song_list = sorted(song_list, key=pick_word_count_for_title, reverse=True)
top10_song_list = sorted_song_list[:10]

# 띄어쓰기나 탭, 개행문자들로 구분된 연속된 문자열을 단어라고 한다면?

# 이방식을 잘 익혀야 요즘 트렌드에 맞는 개발이 가능


### 최댓값 최솟값 max/min
a = [1, 2, 3, 4, 5]
# 최댓값은 5 , 최솟값은 1


# b = []
# 최댓값, 최솟값의 개념이 되려면? 값이 최소 한개는 있어야 한다.

numbers = [1, 2, 5, 4, 3]
max(numbers)

numbers1 = []
max(numbers1, default=0)  # default는 데이터가 비어있을 경우, 정하는 수
# 데이터가 비어있다면 채울 것 ! 0이나 1이나 등등 다 가능.
# 목록데이터가 비어있을때, 대신 반환하는 값!
# max/min 둘다 가능 -> 이제 잘 출력됨


###  대소비교는 정수와 정수 / 문자열과 문자열끼리는 가능!
# 사전이라는 개념에서는 대소비교가 없음.
# 그래서 최댓값을 요청하면 비교할 수 없다는 에러가 뜸
[{"name": "steve", "age": 10}, {"name": "Tom", "age": 8}]
# 만약 근데 여기서 국어성적이나, 키가 가장 작은 학생이든 이런 다양한 기준으로 최댓값/최솟값을 구하고 싶다면?
# 그래서 정렬기준값을 지정해줄 함수를 뽑아주는 것!
