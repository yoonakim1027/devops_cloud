// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set
// reduce -> set -> size

const { melon_data: song_array } = require("./melon_data");



// artist_list => 아티스트만 출력
const artist_list = song_array.map(function (song) {
    return song.artist;
})



// //for (const song1 of songs) {
//     console.log(`[${song1.like}] ${song1.title}`);
// }
/*
var arr = {};
if (!(id in arr)) {
}
else {
}
*/
const count_list = {}
let ok_counter = 0; // 값을 증가시킬거니까 let

for (list of artist_list) { // 100번 for문 돈다 
    if (!(list in count_list)) {
        count_list[list] = 0
    }
    else {
        count_list[list]++;
    }
};

const reducer = (previousValue, currentValue) => previousValue + currentValue;

const filtered_list = Object.values(count_list).filter(
    (value) => (value > 0)
);

console.log(filtered_list.length);


// 중복제거한 값
// const artist_set = new Set(artist_list);


// console.log(`#11 멜론 top100 리스트에 랭크된 가수는 총 ${artist_set.size}팀 입니다.`);

// 만약 새롭게 set으로 중복제거를 한 리스트와
// song_array와 비교해서 ?
// set할때마다 카운트..?
// set을 하면 ? 중복되는 값이 제거되지 ?
// 그때마다 카운트.. 시키면... ? 






