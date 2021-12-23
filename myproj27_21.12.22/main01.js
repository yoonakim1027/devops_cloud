const { melon_data: song_array } = require("./melon_data");


// TODO: #1 like 오름차순으로 정렬
// 출력포맷 : `[좋아요수] 곡명`
// Array의 sort 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort



/* Array의 sort는 
    자신(array)의 순서도 변경하고 자신을 반환
    (파이썬에서의 list의 sort는 자신(list)의 순서만 변경 -> 리턴값 X (None) )

*/

// 자신이 변경됨. 변경되니까 따로 리턴값을 받지 않아도 됨 
song_array.sort(
    (song1, song2) => song1.like - song2.like,
);

/*
song2가 크면 음수를 반환,
song1이 크면 양수를 반환
같으면 0을 반환
둘다 숫자니까 그냥 song1.like - song2.like 


*/

// 자바스크립트의 for of 는 ? 
// 파이썬의 for in과 같음! 
// 여기서는 for ~ of 를 써서 song_array의 값을 하나씩 빼와서 song
for (const song of song_array) {
    console.log(song.like, song.title);
}

// const {like, title} = song; //필요한 필드만 받아오기 ! 


// for (const {like, title} of song_array){
//     console.log(like, title);
} 
