// TODO: #14 방탄소년단의 곡 중에 좋아요 수가 가장 작은 곡명은?
// Array의 filter와 reduce를 활용해주세요.

const { melon_data: song_array } = require("./melon_data");

const reducer = (previousValue, currentValue) => previousValue > currentValue ? previousValue : currentValue;

function filter_bts(song_array) {
    return song_array.artist === "방탄소년단";
}

const bts_filter_result = song_array.filter(filter_bts);

//const arr = bts_filter_list.reduce((a, b) => a > b ? a : b);
const bts_like_list = bts_filter_result.map(function (song) {
    return [song.title, song.like];
});


// 리스트 형식으로 되어있는것을 결과 값으로만 출력됨 
let map = new Map(bts_like_list);

console.log("#14 방탄소년단의 곡 중에 좋아요 수가 가장 작은 곡명은")
console.log([...map.entries()].reduce((pv, cv) => pv[1] < cv[1] ? pv : cv)[0]);

//console.log(`#13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명 : ${arrary_title_words}`);
