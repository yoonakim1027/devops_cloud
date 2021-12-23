const { melon_data: song_array } = require("./melon_data");


// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

// sorting을 위해 존재! 
// is_ascending = True 
const compare_string_for_sort = (string1, string2, is_ascending = true) => {
    if (string1 < string2) return is_ascending ? -1 : 1; // 큰 수를 반환하면? 오름차순 / 작은 수를 반환하면 내림 차순 .
    // 값에 따라 반환하는 값이 달라질 것 
    // is_ascending ? -1: 1 => 참이면 -1 : 거짓이면 1을 반환하겠다.
    else if (string1 > string2) return is_ascending ? 1 : -1;
    else return 0;
};


const popular_song_array = song_array
    .filter(({ like }) => like >= 200_000)
    .sort(
        (song1, song2) => {
            return compare_string(song1.title, song2.title, true)
        });


for (const { like, title, artist } of popular_song_array) {
    console.log(`[${like}] ${title} ${artist}`);
}




song_array
    .filter(({ like }) => like >= 200_000)
    .sort(
        (song1, song2) => {
            if (song1.title < song2.title) {
                return -1;
            }
            else if (song1.title > song2.title) {
                return 1;
            }
            else {
                return 0;
            }




            // 문자열까지 뺄수는 없지만 대소비교는 가능하다! 
            // 오름차순 
            // song1이 song2보다 크다면, 음수를 반환 => 오름차순 정렬 // 양수를 반환하면? 내림차순 
            // song1이 song2보다 작다면, 양수를 반환 => 오름차순 정렬 // 음수를 반환하면? 내림차순 
            // 같다면 0을 반환

            // 내림차순 
            // song1이 song2보다 크다면, 양수를 반환 => 내림차순 정렬 // 양수를 반환하면? 내림차순 
            // song1이 song2보다 작다면, 음수를 반환 => 내림차순 정렬 // 음수를 반환하면? 내림차순 
            // 같다면 0을 반환

        }
    )




