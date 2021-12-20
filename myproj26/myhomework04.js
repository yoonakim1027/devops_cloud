
// 배열의 길이를 구하기 위해서는 legth

// 입력한 인덱스(키)의 밸류 값을 출력해주는 것.
const readlineSync = require('readline-sync'),
    animals = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"],
    index = readlineSync.keyInSelect(animals);
    console.log(animals[index]);



const {question} = require("readline-sync");

const animalsArray = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]


console.log(animalsArray.length); // 배열 길이 구하기
console.log(animalsArray.slice(0,2)); // 0번째 인덱스부터 2전까지.
// ~부터 ~전까지
// for (let i = 0; i <6; i++){
//     console.log(animals1[i]);
// }

//  shuffle라는 이름을 가진 함수는 배열(array)을 인자로 받아서,
//  Array.sort() 기능을 이용해 배열의 요소 순서를 변경합니다.
//  배열의 요소 순서는 0 이상 1 미만의 부동소수점 난수 값을 반환하는 Math.random()를 사용합니다.
//  Math.random()을 통해 반환받은 값에서 0.5를 빼면
//  무작위로 0보다 작은 수를 반환하기 때문에
//  Array.sort()에 식으로 사용하면 배열의 요소 순서가 무작위로 변경됩니다.

function shuffle(array){
    array.sort(()=> Math.random()- 0.5);
}

shuffle(animalsArray);


const count = 0;

