// TODO: #3 좋아요수 top10을 출력
// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

const songs = song_array.sort(
    (song_array1, song_array2) => {
        return song_array2.like - song_array1.like;
    }
);

console.log("<<< 좋아요 수 Top10을 출력 >>>> ")
for (const top10_songs of songs.slice(0, 10)) {
    console.log(`[${top10_songs.like}] ${top10_songs.title} ${top10_songs.artist}`);
}