const tom = {
    name: "tom",
    age: 10,
    region: "Daejeon",
}
// 파이썬의 사전보다 더 광범위한 느낌 -> 객체, 오브젝트라고 함 
const name = tom.name;
const age = tom['age'];

//값을 꺼내올건데, 키는? 
const { name1 } = tom;
// tom변수에서 name값만 빼논다는 것
// -> 키로서도 활용되고 변수로서도 활용 됨 


// 키명과 저장할 변수명이 같은 경우 
// const {age} = age;
// const {name, age} = tom;

// 어떤 객체에서, 내가 원하는 키에 해당되는 값만 뽑아오고자 할 때 사용



// 키 name을 읽어와서 otherName이라는 변수에 저장 
const { name: otherName } = tom;
// tom에서 name이라는 키를 가져와서 otherName이라는 변수에 저장하는 것

console.log(otherName);
// 객체에서 name이라는 값을 가져와서 otherName이라는 변수에 저장
// 참고할 변수는 tom



// 완전이 똑같이 복사해서 똑같이 복사 -> 깊은 복사
// 얕은 복사는 얘의 이름만 똑같이 ~ object1을 얕은 복사를 하면? object2가 생성.
// object1의 값을 변경을 하면? object2의 값도 바뀜.

// 얕은 복사는 그림자 분신술
// 깊은 복사는 쌍둥이 


// 객체 : 좀 더 넓은 의미
// 객체는 사전이 아님! 
// 훨씬 더 넓은 의미 



const steve = {
    name: {
        first: "Steve",
        last: "jobs",
    },
    age: 10,
    region: "Daejeon",
}

const { name: otherName1 } = steve;
console.log(otherName1);


const { name: { first } } = steve;
// name이라는 객체안의 first라는 키를 읽어와서
// first라는 이름으로 변수를 저장하겠다.

console.log(first);
//first라는 키지만, 저장하는 변수명은 firstname이라고 하고싶다면?

const { name: { first: firstName } } = steve;
console.log(firstName);

