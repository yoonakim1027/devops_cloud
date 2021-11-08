import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

for song_dict in sorted(song_list):
    print(song_dict)
