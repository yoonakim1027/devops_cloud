// TODO: #4 좋아요수가 200,000 이상인 곡명만 출력하기
// Array의 filter 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`



const { melon_data: song_array } = require("./melon_data");

function like_filter(song_array) {
    return song_array.like >= 200000;
}

const like_filter_result = song_array.filter(like_filter);


console.log("#4. 좋아요수가 200,000 이상인 곡명만 출력하기")
for (const like_20 of like_filter_result) {
    console.log(`[${like_20.like}] ${like_20.title} : ${like_20.artist}`);
}