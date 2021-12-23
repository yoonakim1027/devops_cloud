const { melon_data: song_array } = require("./melon_data");


// TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요?
// Set와 속성 .size를 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set

/*
파이썬에서는 .set이라는 중복제거 함수를 쓰면 됨
자바스크립트에서는 new Set() 이렇게 만들어야 함.


*/

const artist_array = song_array
    .map(({ artist }) => artist);


const artist_set = new Set(artist_array);
// 집합은 중복이 제거가 되기때문에 length가 아니라 size
// 집합이니까 길이가 없음 
console.log(artist_set.size);
// 집합에는 .length 못쓴다
// 각 어떤 함수, 속성이 지원되는지는? .누르고 밑에 뜨는 목록들로 확인할 수 있음



const artist_count = song_array
    //.map(({artist})=> artist)
    .reduce((acc, { artist }) => {
        acc.add(artist);
        return acc;
        // artist 이름으로 채워진 집합이 채워짐.
    }, new Set())
    .size;
// reduce가 집합을 리턴하기 때문에, .size

console.log(`artist_c;ount: ${artist_count}`);









const artist_array1 = song_array.map(({ artist }) => artist);
const total1 = new Set(artist_array1).size;

console.log(`랭크된 가수는 ${total1}팀입니다.`);


const total2 = song_array
    .reduce((acc, { artist }) => {
        acc.add(artist);
        return acc;
    }, new Set())
    .size;

console.log(`랭크된 가수는 ${total2}팀입니다.`);
