// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`
const { melon_data: song_array } = require("./melon_data");

function like_filter(song_array) {
    return song_array.like >= 200000;
}

const like_filter_result = song_array.filter(like_filter);


// 곡명 오름차순 정렬
like_filter_result.sort(function (a, b) { 
    return a.title < b.title ? -1 : a.title > b.title ? 1 : 0;
});


// 출력포맷 : `[좋아요수] 곡명 가수명`

console.log("#5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬")
for (const like_20 of like_filter_result) {
    console.log(`[${like_20.like}] ${like_20.title} : ${like_20.artist}`);
}





// const title_sort = like_filter_result.sort(
//     (like_filter_result1, like_filter_result2) => {
//         return like_filter_result1.title - like_filter_result2.title;
//     }

// );




// for (const like_20 of array.title) {
//     console.log(`[${like_20.like}] ${like_20.title} : ${like_20.artist}`);
// }

// console.log("#5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬")
// for (const like_20_sort of like_sort) {
//     console.log(`[${like_20_sort.like}] ${like_20_sort.title} : ${like_20_sort.artist}`);
// }

