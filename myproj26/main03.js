// 객체
// 앞에 const나 let을 꼭 ! 
//const age = "나이"

// const tom = {
//     "name": "Tom",
//     // "age": 10,

//     // 대괄호가 사용 O
//     // 키가 들어가면? 왼쪽은 계산하라는 뜻
//     //['ag' + 'e']: 10,
//     [age]: 10,

//     // 키로는 array(배열)을 쓰지 않는다.
//     // eval(평가)로는 씀

// }

// 2. 
// console.log(tom);


// const name = "Tom";
// const age = 10;
// const tom1 = {
//     name, // name : name
//     age, // age : age 
// };

// name : name,
// age :age,
// 키와 밸류 이름이 같으면 
// 생략이 가능 

// 파이썬의 사전과 같음 

// 파이썬은 self가 있음
// 다른 언어에서는 this
// this = 현재의 인스턴스(자기 자신)

// 클래스를 통해 인스턴스를 만들었음
// 자바 스크립트는 클래스가 없어도 인스턴스를 만들 수 있음


const name = "Tom";
const age = 10;
const tom1 = {
    name: name,
    age: age,
    print: function () {
        console.log(this.name, this.age)
        // 출력을 할 때 값만 출력 
    }
    // 현재 tom1에 있는 name, age가 프린트됨
};

tom1.print();

//상수는 값을 변경할 수 없음 



const name1 = "Tom";
const age1 = 10;
const tom2 = {
    name: name1,
    age: age1,
    print() {
        console.log(`안녕. 나는 ${this.name}이야. ${this.age}살이지.`);
    }
    // 현재 tom1에 있는 name, age가 프린트됨
};

tom2.print();


// js 에서 파이썬 처럼 f스트링 문법을 사용하려면 ?
// 작은따옴표가 아니라, `` 백핏! 사용 !! 


