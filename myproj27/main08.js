// TODO: #8 곡명에 "사랑"이 포함된 곡들의 곡명 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

const { melon_data: song_array } = require("./melon_data");


// filter, map

const love_title_filter = song_array.filter(
    function (song) {
        return song.title.includes("사랑")
    }
)

const love_title_list = love_title_filter.map(function (song) {
    return song.title
})

console.log("#8 곡명에 '사랑'이 포함된 곡들의 곡명 배열을 구성");
console.log(love_title_list);