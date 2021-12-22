// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

const { melon_data: song_array } = require("./melon_data");


// string.length
// .length는 문자열의 길이를 반환하는 속성 


// 곡 글자 수 
// 새로 배열 생성 (우선 곡명만 출력)
console.log("<<<<< 곡 글자 수 >>>>>>>")
const arrary_title_like = song_array.map(function (obj) {
    let array_total = {};
    array_total[obj.title] = obj.title.length;
    return array_total;
});

console.log(arrary_title_like);

// 곡명 / 단어수 문자열로 출력하기 

// song_array.map(function (song) -> for i in range의 i처럼 range범위 안의 값이 하나씩 들어가는 것-> 이름은 파이썬 처럼 의미있게 
console.log("<<<<<< 곡 단어 수 >>>>>>") // 배열에서 map을 통해서 새로운 배열 생성 -> 배열.map(function(배열 항목 하나씩 빼오는 것.. ? ㅎ))
const arrary_title_words = song_array.map(function (song) {
    const word_count = song.title.split(" ").length;
    return `${song.title} / ${word_count}`;
});


// #6 "곡명 / 단어수" 
console.log(arrary_title_words);



// //
// console.log("<<<<<< 곡 단어 수 >>>>>>")
// const arrary_title_like_words = song_array.map(function (obj) {
//     let array_total_words = {};
//     array_total_words[obj.title] = obj.title.split(" ").length;
//     return array_total_words;
// });