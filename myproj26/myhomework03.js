/* npm install readline-sync
-> 이는 꼭 !! 꼭 사용하고자 하는 폴더에서 설치해야 한다

*
* */

// 필요한 것 : 우선 랜덤값 인출을 위한 리스트
const readlineSync = require("readline-sync");
const animals = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"];

// 현재 시간 출력
// let -> 선언한 다음에 바뀔 수 있는 변수
// const -> 상수

let startTime = new Date();
console.log("현재 시작 시간 : " + startTime);


function shuffle(array){
    array.sort(()=> Math.random()- 0.5);
}
shuffle(animals);

let counter = 0;
// 파이썬의 f스트링 같은 용법 : `${변수명}`

for (let i = 0; i <5; i++){
    let shuffleAnimal = animals[i];
    console.log("♥ 따라 입력해보세요 ♥");
    const {question} = require("readline-sync");
    const input = question(`${shuffleAnimal} : ` );

    if (shuffleAnimal === input) {
        counter++;
        console.log("정확합니다.");
    }
    else {
        console.log("오타가 있어요.");
    }

}
i = 0;
//STtime
let finishTime = new Date();
let FTtime = finishTime.getTime();
let STtime = startTime.getTime();

// Math.floor -> 소숫점 자리 삭제. (올림, 내림 X 그냥 삭제)
let number = Math.floor((FTtime - STtime) / 1000);

console.log(`총 ${counter}번 성공하셨습니다.`);

console.log(`총 ${number}초가 걸리셨어요.`);


