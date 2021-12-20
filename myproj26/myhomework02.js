// timestamp = +new Date().getTime();
// 초단위로 하는 것

// timestampSecond =Math.floor(+new Date()/1000);
//
//
// console.log(timestampSecond);
// 현재 timestamp
const myDate = new Date();
console.log(myDate);


// 현재 시간 반환 -> 몇초가 걸렸는지 이니까 초를 반환하는 것이 나음
// 초 반환하는 것은 getTime()

const myTime = new Date();
console.log("현재 시각 : " + myTime.getTime());


// slice() 메서드는 어떤 배열의 begin 부터 end 까지(end 미포함)에 대한 얕은 복사본을 새로운 배열 객체로 반환합니다.
// 원본 배열은 바뀌지 않습니다.
const animals = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"];

const animal = animals.slice(1,3);
console.log(animal);

// javascript에서의  for 반목문

// 리스트 같은 객체에 있는 값을 빼오기
for (const key in animals) {
    console.log(`${key}:${animals[key]}`);
}
//index = readlineSync.keyInSelect(animals1, "동물을 입력해주세요:");
// keyInSelect는 인덱스 값으로 입력한 값을 불러오는 것

const readlineSync = require('readline-sync'),
    animals1 = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"],
    index = readlineSync.keyInSelect(animals1);


