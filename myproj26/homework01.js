const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]



// 자바스크립트에서 array를 슬라이싱해서 5개만 뽑기

// TODO : shuffle 


// TODO :  slicing 

// TODO : 현재 timestamp 


// TODO : input (한줄 입력) 받기 
// python input은 자바스크립트에 없음
// 그래서 설치할 것은 ?
// readline-sync 라이브러리 설치

// 프로젝트 소스코드가 있는 폴더까지 이동을 한 뒤 !~~~
// pip는 아무곳에나 해도 되지만~
// npm은 설치 명령을 할 폴더에 설치!! 
// 위치가 중요하다 
// 이동을 한 후, 
// npm install readline-sync
// 프로젝트 경로에서만 설치!!


// 3번 문제 : readlineSync 사용해서 input값 받기

// var 대신 const를 쓰면 돼 
const { question } = require("readline-sync");
// question 이라는 함수에 다이렉트로 접근할 수 있음
// 이를 input하듯이 쓰면 돼
const number = question("Enter a number:");
console.log("당신의 번호는" + number);

// 인풋 값 받기
const readlineSync = require('readline-sync'),
    animals = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"],
    index = readlineSync.keyInSelect(animals, "which animal?");
console.log(animals[index] + "가 당신이 선택한 동물입니다.");



// 0이상 1 미만 랜덤 수(실수) 출력

