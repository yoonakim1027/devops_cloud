const { melon_data: song_array } = require("./melon_data");


// TODO: #4 좋아요수가 200,000 이상인 곡명만 출력하기

// filter를 사용해야 함 
// Array의 filter 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const filtered_song_array2 = song_array
    .filter(song => song.like >= 200_000) // javascripts에서도 파이썬 처럼 숫자 중간에 언더바를 지원 ! 
// filter는 원본이 바뀌지 않고, filter를 적용한 array가 생섯ㅇ

const filtered_song_array = song_array
    .filter(({ like }) => like >= 200_000);


for (const song of filtered_song_array) {
    console.log(`[${song.like}] ${song.title} ${song.artist}`);
}
