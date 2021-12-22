// TODO: #7 방탄소년단의 곡명 문자열로 구성된 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

const { melon_data: song_array } = require("./melon_data");


function filter_bts(song_array) {
    return song_array.artist === "방탄소년단";
}

console.log("<<<<<< 방탄소년단 곡명 출력 >>>>>>") // 배열에서 map을 통해서 새로운 배열 생성 -> 배열.map(function(배열 항목 하나씩 빼오는 것.. ? ㅎ))
// filter랑 map 사용 

const bts_filter_result = song_array.filter(filter_bts);

const arrary_title = bts_filter_result.map(function (song) {
    let bts_title_list = [];
    bts_title_list.push(song.title);
    return bts_title_list;
});


console.log(arrary_title);