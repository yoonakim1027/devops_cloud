// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
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


let map = new Map(bts_like_list);

console.log("#13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은")
console.log([...map.entries()].reduce((pv, cv) => pv[1] > cv[1] ? pv : cv)[0]);

//console.log(`#13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명 : ${arrary_title_words}`);
// ... 파이썬에서 ** 언패킹하는것.

// 0은 song.title, 1은 song.like




/*
const reducer = (pv, cv) => pv.like > cv.like ? pv : cv;
? = if 
: = else
0번인자 > 1번인자 => 비교 후, True면(왼쪽값이 더 클경우)=> 0번 인자를 반환
그러면? 0번 인자가 -> pv가 된다
0,1,2,3,4,5
0번과 1번을 비교 -> 이긴 값이 pv 또 싸우는 애가 2(cv) 
이걸 끝날때까지 계속 반복
=> 최종 리턴값이 가장 큰애? 
pv가 cv보다 클경우에 ture의 값은 pv / false일 경우에 cv
큰 값을 리턴했기 때문에? 끝나면 가장 큰 값이 리턴이 되는 것.
<< 작은 값을 얻기 위해서는? >> 
? True : False 니까 , 앞에 부등호를 반대로 바꿔줘도 되고 
물음표 뒤의 pv와 cv의 순서를 바꿔주면 됨 
*/
