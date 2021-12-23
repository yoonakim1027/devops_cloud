const { melon_data: song_array } = require("./melon_data");


// TOOD: #2 방탄소년단의 곡명만 출력 -> 지정 곡명만 filtering 하겠다
// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

/*

const bts_song_array = song_array // === 세개를 써야 좀 더 정확한 비교 
    .filter(song => song.artist === "방탄소년단") // True / False를 출력 
// 그냥 변수명만 쓰면 소괄호 없이 song만 써도 되는데 ?
// song.의 .artist를 뽑고 싶은거면 ({중괄호}) 

*/

const filtered_song_array = song_array.filter(
    ({ artist }) => artist === "방탄소년단"
);


for (const song of filtered_song_array) {
    console.log(song.like, song.title);
}
