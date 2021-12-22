// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set
// reduce -> set -> size

const { melon_data: song_array } = require("./melon_data");



// artist_list => 아티스트만 출력
const artist_list = song_array.map(function (song) {
    return song.artist;
})


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





