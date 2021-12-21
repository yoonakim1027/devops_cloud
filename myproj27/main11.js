// TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요?
// Set와 속성 .size를 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set

// reduce -> set -> size

const { melon_data: song_array } = require("./melon_data");

// artist만 출력하기 
const artist_list = song_array.map(function (song) {
    return song.artist;
})

const artist_set = new Set(artist_list);

console.log(`#11 멜론 top100 리스트에 랭크된 가수는 총 ${artist_set.size}팀 입니다.`);