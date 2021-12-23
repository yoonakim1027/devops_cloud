const { melon_data: song_array } = require("./melon_data");


// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

//<<<<<<<<<< 방법 1 >>>>>>>>>>>>
const title_array = song_array
    .map(({ title }) => `${title} / ${title.split(/\s+/).length}`);


for (const title of title_array) {
    console.log(title);
}

/* map의 결과를 reducer로 구현 
항목은 100개
각각의 항목에 대해서, 1번 항목(object)을 문자열로 변환 -> 이를 할 때 map을 사용
1개의 song object를 문자열로 변환 
각각의 array를 처리하는 것은?  map 함수가 하는것
우리가 할일은? 한개의 오브젝트를 문자열로 변경해서 리턴해주면 됨
그 문자열로 배열을 만드는 것은 map이 하는 것
우리는 그거를 문자열로 변환해주는 함수만 만들면 됨 ! 
*/

const title_array1 = song_array.map(
    (song) => {
        const word_count = song.title.trim().split(/\s+/).length; // 좌우 공백제거 + split
        return `${song.title} / ${word_count}`;
    },
);


/* 여기에 word(단어)가 몇 개가 있는지 count를 해줄 것이 필요 
 파이썬에서는 title.split를 써주면 되지만? 
split의 기본은 white spaces 화이트 스페이스.
.split() 안에 아무것도 안쓰면? 화이트 스페이스를 기준으로 알아서 해줌 
*/

/* 
그런데 자바스크립트에서는? 인자를 지정해줘야 함 
문자열 유형의 separator 가 두 글자 이상이면? 그 부분 문자열 전체가 일치해야 끊어진다.
문자열이나 정규표현식을 받을 수 있음 

연속된 공백도 하나의 구분자로 처리하고 싶다면? 
이러면 정규표현식을 써줘야 함 
파이썬의 정규표현식은 보통 문자열로 씀 


** 정규표현식
/\s+/
+ : 1회 이상 
s : 모든 스페이스 
=> 전체 뜻 : 모든 스페이스를 통틀어서 하나로 치겠다 
화이트스페이스가 1회이상 반복 되면 이를 새로운 구분자로 해서 지정하겠다.

.trim() 좌우 공백 제거
.trim().split(/\s+/)
*/

//<<<<<<<<<< 방법 2 >>>>>>>>>>>>
const title_array2 = song_array.map(
    (song) => {
        const word_count = song.title.trim().split(/\s+/).length; // 좌우 공백제거 + split
        return {
            title,
            word_count, // 이렇게가 새로운 object가 생성된 것 
        };
    },
);

for (const title_obj of title_array2) {
    console.log(title_obj); // title, word_count
}



//<<<<<<<<<<< 방법 3 >>>>>>>>>>>>
// 기존 song_array 배열에서
// word_count라는 컬럼을 추가하고 싶다.
const new_song_array = song_array.map(
    (song) => {
        const word_count = song.title.trim().split(/\s+/).length; // 좌우 공백제거 + split
        return {
            ...song, // song의 모든 key value를 가진 상태에서, 
            word_count: word_count, // 새로운 word_count 컬럼을 추가
        };
    },
);

for (const new_song of new_song_array) {
    console.log(new_song); // 기존의 song에 word_count 컬럼 추가
}



