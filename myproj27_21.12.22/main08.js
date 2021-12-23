const { melon_data: song_array } = require("./melon_data");


// TODO: #8 곡명에 "사랑"이 포함된 곡들의 곡명 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]
/*
filter 하는 방법만 바뀌고, map을 하는 과정은 같음 -> filter를 잘 해줘야 함

파이썬에서는? "사랑"in song['title']

자바스크립트에서는 ? 
indexOf =>  song['title'].indexOf(아주 오래전부터 문자열에서 지원되던 것)
            index는 항상 0부터 시작. 만약 포함되어있지 않다면? 이를 -1로 표현.
            그래서 찾으려면 ? 
            song['title'].indexOf("사랑") >-1 -> -1이라는건 없다는 거니까 -1보다 큰 것을 찾는 것 

include =>  song['title'].incldue("사랑") -> True/False를 반환 이게 좀 더 최신! 

            

*/

// 하위 호환성을 보장해주는 라이브러리 
const love_song = song_array// 각 song에 대한 정보들이 들어있음
    .filter(
        ({ title }) => title.includes("사랑") // 나중에 업그레이드 되다가~ 모든 브라우저가  es6를 지원하게 됬을때` 
    )
    .map(
        ({ title }) => title
    );


console.log(love_song);





const lovesong_title_array = song_array
    .filter(({ title }) => title.includes("사랑"))
    .map(({ title }) => title);


for (const title of lovesong_title_array) {
    console.log(title);
}
