//21.12.21

// // 내장함수 map 사용 
// // 새로운 Array(배열), 제곱수로 구성된 숫자 배열
// function mapper(number) {
//     return number ** 2;
// }
// // 자바스크립트는 애로우 펑션이 항상=, =>

// // 1버전
// const mapper = (number) => {
//     return number ** 2;
// }
// // 2버전
// const mapper = (number) => number ** 2;

// // 3버전( 이렇게 간단하게도 쓸 수 있다.)
// // 인자가 하나일 경우엔 괄호를 안써도 된다! 
// const mapper = number => number ** 2;

// const new_numbers = numbers.map(mapper);
// console.log(new_numbers);



// const new_numbers = numbers.map(
//     number => number ** 2
// );



// ----- sorted
/*
1) Array의 sort 사용 

*/

const numbers = [1, 2, 3, 4, 5];

// Array의 sort
function make_random_value(number1, number2) {
    return Math.random();
    // 0과 1의 범위 사이에서 랜덤 수 하나를 만들어줌 
}

numbers.map(
    (number) => ({ number, 기준값: Math.random() }
    ),

).sort(
    (value1, value2) => {
        return value1.기준값 - value2.기준값;
    }
).map(
    (value) => value.number
);


// 체이닝


// const number1 = number.map(
//     (number) => ({number, 기준값 : Math.random()})
// )

// 자바 스크립트의 sort: 원본을 수정한다 
//(파이썬의 sorted는 원본을 수정하지 않는다)

// a - b ->

const numbers = [1, 2, 3, 4, 5]; // [31, 89, 24, 81, 46];

// Array의 sort
function make_random_value(number1, number2) {
    return Math.random();
}

const number1 = numbers.map(
    (number) => ({ number, 기준값: Math.random() }),
);

const number2 = number1.sort(
    (value1, value2) => {
        return value1.기준값 - value2.기준값;
    }
);

const number3 = number2.map(
    (value) => value.number
);

console.log(new_numbers);