const { melon_data: song_array } = require("./melon_data");


/* TODO: #3 좋아요수 top10을 출력 
// -> 좋아요 수에 대한 내림차순 정렬 
여기서 처음 10개를 뽑아내면 됨 
Array의 sort 활용

- 좋아요 수에 대한 내림차순 정렬 - > 처음 10개
- 좋아요 수에 대한 오름차순 정렬 - > 마지막 10개 (reverse 뒤집음 )

 출력포맷 : `[좋아요수] 곡명 가수명`
*/

const like_top10 = song_array
    .sort(
        (song1, song2) => song2.like - song1.like, // 빼기의 순서를 바꿔주면? 내림차순 !
    )
    .slice(0, 10); // 처음 열개는 (0,10) / (-10) 뒤에서 열개 
// 슬라이스는 꼭 !! (0,10) 앞인자에 0도 써줘야함(파이썬은 생략 가능이지만~)    
// sort 자체가 array도 변경 + 자신도 리턴 


// 여러 문자열을 섞어서 문자열 출력할때에는 백핏 `` 사용 


const top10_song_array = song_array.sort(
    (song1, song2) => song2.like - song1.like
).slice(0, 10);

// 1번째방법
// let i = 1;
// for (const {like, title, artist} of like_top10) {
//     console.log(`${i} [${like}] ${title} ${artist}`)
//     i ++;
// }


//2번째 방법
// entries() -> 인덱스 생성 -> 0부터 시작 시작값을 정해줄 수는 없음 
for (const [index, song] of top10_song_array.entries()) {
    const rank = index + 1; // 랭크는 1부터 시작해야 하니까 +1을 해줌 
    console.log(`${rank} [${song.like}] ${song.title} by ${song.artist}`);
}


//3번째 방법
// for (const [index,{like, title, artist}] of like_top10.entries()) {
//     console.log(`${index+1} [${like}] ${title} ${artist}`)
//     i ++;
// }








