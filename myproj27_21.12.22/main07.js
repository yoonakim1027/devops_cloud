const { melon_data: song_array } = require("./melon_data");


// TODO: #7 방탄소년단의 곡명 문자열로 구성된 배열을 구성해주세요.
// 방탄 소년단의 곡명만 필터링 
// artist 컬럼으로 필터링
// 그다음에 곡명만 map / reduce를 사용해서 새 array 생성 

// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]


const bts_title_array1 = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .map(({ title }) => title);


for (const title of bts_title_array1) {
    console.log(title);
}



// map 버전 ------------------
// 항상 간소화가 좋은 코드는 아님! 가독성이 중요하다.
// 항상 짧게 만들기만 하지말고?
// 내가 이코드를 봤을때? 다른 사람들이 이 코드를 봤을 때 이해가 되는 것이 중요
const bts_title_array = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .map(({ title }) => title);



// reduce 버전 -----------------
/*
reduce() -> 여러 분야에서 다양하게 활용되는 개념! 
- map reduce
map은 순수하게 변환 . 
reduce가 합치는 역할 => 분산 네트워킹 

누산기(acc) -> 
현재 값(cur)

[1,2,3,4,5] -> 이를 합하려면? 
초기값이 필요함.
초기값은 먼저 acc라는 변수에 0이 들어감.
이제 그럼 1번째 값인 1이 들어옴
계산을 함
그럼 acc 는 1로 변경
그다음에 두번재 값인 2를 가져옴 
그러면 acc는 3
그다음 값 3을 가져와서 연산을 해서 결과는? 6
그다음 4를 가져와서 연산을 하면 결과는 10.. 이렇게 결과는 15


*/


const numbers = [1, 2, 3, 4, 5]
// numbers는 array이니까 reduce()사용 가능
const result_sum = numbers.reduce((acc, number) => {
    acc += number;
    return acc;
}, 0);  // <- 여기부분의 0이 초기값! ! 

// reduce의 인자는 항상 두개
// 첫번재는 누적을 해나갈 acc의 값 -> 이름은 중요하지 않음 ~
// 두번째는 각 값이 하나씩 넘어오게되는 값이 저장되는 cur(number)
// 하나의 상황만 함수로서 구현해주면 됨 ! 
// 우리가 어떤 값을 계산하고 리턴하면? acc값이 이 리턴한 값으로 변경
// 이런식으로 계속 acc의 값을 누적해나가게 됨 

console.log(`합 : ${result_sum}`);


// 제곱하고싶다면?
const numbers1 = [1, 2, 3, 4, 5];
const new_numbers = numbers1.map(number => number * number);
console.log(new_numbers);


// 첫번째 인자는 함수, 최종 결과가 배열이니까 빈 배열을 옆에 만들어주면 됨 
// numbers1.reduce((,)=> {},[])
const new_numbers1 = numbers1.reduce((acc, number) => {
    acc.push(number * number);
    return acc;
}, []); // array(파이썬으로 치면 list)
console.log(new_numbers1);


// 여기서 마지막에 들어갈 {}이 초기값이라는 소리임
const new_number_object = numbers1.reduce((acc, number) => {
    acc[number] = number * number;
    return acc;
}, {}); // (1) 파이썬의 사전 = 자바스크립트의 객체(키 : 값이 존재), (2)함수의 시작과 끝을 알림  
console.log(new_number_object);


