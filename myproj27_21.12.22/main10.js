const { melon_data: song_array } = require("./melon_data");


// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce

/*
파이썬에서는 sum이 있지만?
자바스크립트에서는 reduce를 사용해야 함 
.reduce(누적값, 항상받는 항목값) => {}, 0(초기값) 

*/


Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
}

const result = song_array
    .filter(
        ({ artist }) => artist === "방탄소년단"

    )

    .map(({ like }) => like)
    .sum();

console.log("result : ", result);


const like_total = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .reduce((acc, song) => acc + song.like, 0);


console.log(`좋아요 총 합 : ${like_total}`);


song_array
    .filter(
        ({ artist }) => artist === "방탄소년단"
    )
    .reduce((acc, { like }) => acc + like, 0);
    // 여기서 마지막의 0은 초기값!
    // 더할거니까 {}, []를 안쓰고 0 ! 
