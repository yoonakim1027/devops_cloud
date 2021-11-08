import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        # print(song_dict["artist"], song_dict["title"], song_dict["like"])

        # 1번
        line = "{}, {}, {}".format(
            song_dict["artist"], song_dict["title"], song_dict["like"]
        )
        # 2번
        line = "{}, {}, {}".format(
            가수명=song_dict["artist"], 곡명=song_dict["title"], 좋아요수=song_dict["like"]
        )  # 왼쪽이 이름으로 지정된 것.

        # 3번 키 이름과 같은 이름 지정 후 {}안에 이름 넣기
        line = "{artist}, {title}, {like}".format(
            artist=song_dict["artist"], title=song_dict["title"], like=song_dict["like"]
        )

        # 4번 unpack arguments 사전에 한에서만 사전의 키밸류 값을 풀어서 키워드 인자로 포맷이라는 함수를 넘겨달라
        # 이걸 제일 많이쓰고, 제일 다양하게 많이쓰임

        line = "{artist}, {title}, {like}".format(**song_dict)
        print(line)
