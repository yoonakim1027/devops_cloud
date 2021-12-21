// TOOD: #2 방탄소년단의 곡명만 출력
// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용

//filter() 메서드:  주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환



// melon_data가 저장된 변수 : song_array
const { melon_data: song_array } = require("./melon_data");


// 방탄소년단만 추려낼 각 요소를 시험할 함수 
function bts_title(song_array) {
    return song_array.artist === "방탄소년단";
}


// filter를 적용한 변수 result 
const bts_filter_result = song_array.filter(bts_title);


// 결과값을 출력할 for문 
// 출력포맷 : `가수명 곡명 좋아요수`
for (const bts of bts_filter_result) {
    console.log(`[${bts.artist}] ${bts.title} >>>  ${bts.like}`);
}


// title, album, artist, rank, like 