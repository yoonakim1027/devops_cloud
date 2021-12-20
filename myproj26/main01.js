// 옛날 문법 -> var 하나로 변수 선언이 가능.
// var name = "김유나"; //선언 
// name = "김초롱"; //변경 
// console.log("hello world");


// 현재는 두 개의 정의로 가능 


// 옛날꺼에는 var를 쓰지만, 최신 자바 스크립트 문법에서는 let을 씀 
// 변수 정의 
// 변수를 선언하고, 변수의 값 변경도 가능.
let name = "김유나"; //선언
name = "김초롱"; //변경

// const 는 상수 정의 -> 상수의 값 변경이 불가능 (Constant)
const age = 10;

console.log(name, age);


// 제어 구조 
const number = 10;
if (number % 2 === 0) {
    console.log("짝수");
}

else {
    console.log("홀수");
}




// 반복문
// i++ -> i 변수의 값을 1씩 증가시킨다.
for (let i = 1; i < 11; i++) {
    console.log(i); // 코드 블럭을 실행하면? 3번째 콤마 부분으로가서 i에 1씩 증가 
}



// i++ 는 1씩 증가
// i를 2씩 증가하고 싶다면 파이썬에서처럼 
// i +=2

for (let i = 1; i < 11; i += 2) {
    console.log(i);
}

// 파이썬에서는 중괄호를 사용할 일이 별로 없었는데~ 


// 함수

function mysum(x, y) {
    return x + y;
}

// 호출방법은 같다 ! 


// 이게 익명함수
function mysum(x, y) {
    return x + y;

};

// 그냥 함수 정의 
const mysum2 = function (x, y) {
    return x + y;
};



// arrow function
const mysum3 = (x, y) => {
    return x + y;
};

// 세미콜론 꼭 써주기


// mysum2, mysum4 함수들을 가장 많이 쓸 것 
const mysum4 = (x, y) => x + y;



// == // 추상적 같음
// === // 엄격한 같음 


// js에는 sum 문법이 없음 ! 
function mysum5(x, y, ...args) {
    console.log(x, y, args);

};

mysum5(1, 2, 3, 4, 5);


function reducer(preValue, currentValue) {
    return preValue + currentValue;
}

// 우리가 더하려는 함수는? 
const result = [1, 2, 3, 4, 5].reduce(reducer, 0); // array 배열 
// .reduce에 (reducer함수를 넘겨주고, 초기값은 0)

console.log(result);


const result2 = [1, 2, 3, 4, 5].reduce((preValue, currentValue) => {
    return preValue + currentValue;
}, 0);

console.log(result2);


const result3 = [1, 2, 3, 4, 5].reduce(
    (preValue, currentValue) => preValue + currentValue,
    0); // 0은 초기값 

console.log(result3);

