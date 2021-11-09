### (1) 좋아요 수로 TOP10 곡명 리스트를 만들어보자
# 내림차순으로 정렬하고 처음 부터 10개를 출력하면 이게 TOP 10 !!!


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
