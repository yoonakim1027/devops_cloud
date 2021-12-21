//자바 스크립트의 언패킹 문법

function mysum3(x, y, z) {
    return x + y * 10 + z * 100;
}

// 위치인자
mysum3(1, 2, 3)

// (mysum3(y=1,x=2,z=3)자바스크립트에는 키워드 인자 문법이 없음 

// 키워드인자랑 비슷하게 사용하는 문법은 있음
// 파이썬의 keyword arguments와 비슷하게 사용하는 코드 


// mysum3({x:1,y:2,z:3})
// 그러나 이것은 인자를 통채로 1개로만 넘기는거라서 호출할 수가 없음


// 이렇게는 가능 ! 중괄호로 덮어주면~ 
const { x, y, z } = { x: 1, y: 2, z: 3 };

function mysum3({ x, y, z }) {
    return x + y * 10 + z * 100;
}

// 인자를 넘길때도 객체로 넘기기~ ! 

// 클래스 컴포넌트 -> 함수 컴포넌트
// 각각 함수의 인자마다 이름을 부여하는 것이 필요해지고~

// 함수정의는 그래서 거의 function 함수명({}) 이렇게 안에 중괄호


const people = [
    { name: 'Tom', age: 10, region: 'Seoul' },
    { name: 'Steve', age: 12, region: 'Pusan' }
];

// 파이썬의 for와 비슷
// for (const person of people) {
//     console.log(person)
// }
// // 객체를 하나씩 받아와서 출력하게 됨 


for (const {name, age}of people){
    console.log(name, age);
};

// 위와 밑은 같음! 
// for (const {name, age}of people){
//     console.log(person.name, person.age);
// };