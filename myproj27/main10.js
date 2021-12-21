// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce


const { melon_data: song_array } = require("./melon_data");

const reducer = (previousValue, currentValue) => previousValue + currentValue;


const bts_filter = song_array.filter(
    function (song) {
        return song.artist === "방탄소년단";
    }
)

const bts_filter_list = bts_filter.map(function (song) {
    return song.like;
})

console.log(`#10 방탄소년단의 좋아요의 총 합 : ${bts_filter_list.reduce(reducer)}`);
