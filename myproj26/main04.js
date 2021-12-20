// 객체 복사

const obj = { value1: 10 };

// 키가 문자열로 들어간것과 같음
// 'value1' 이렇게 

// 키에 접근하려면 ?사전처럼
obj['value1']


obj.value1 // 이렇게도 접근 가능 

const obj0 = { value1: 10, "p-1": 20, };

// 변수명으로 사용할 수 없는 키값은 항상 쌍따옴표로 접근해야 함 
obj0['p-1'] // 이거는 가능
// obj1.p-1 // 이거는 불가능 

// indexError, KeyError (파이썬) 
// -> no error, undefined  js에서는 에러가 없다 .

// 파이썬에선 Exception 
// js에서는 no error, undefined, null(파이썬에서의 none과 유사)
// undefined 는 자바스크립트에만 있는 개념. 정의되지 않음

// 지정 속성이 없으면 undefined를 반환 
// 파이썬에서는 어떤 함수가 리턴 값이 없으면 None을 대신 리턴
// js에서는 리턴값이 없으면 undefined를 반환

// = js에서는 함수가 아무런 값도 리턴하지 않으면 undefined를 반환




/// 객체 복사

const obj1 = { value1: 10 };
const obj2 = obj1; // 얕은 복사 

// obj1을 통해서 값을 바꾸고, obj2를 보면 변경된 값으로 변경됨

// 얕은 복사의 좋은 점은? 기존의 변수 값을 복제할 필요가 없어서 변수생성이 빠름
// 적절하게 얕은 복사를 해줘야~ 어플리케이션이 빠릿하게 동작을 함 



// 깊은 복사를 하는 방법 중의 하나. 깊은 복사를 지원하는 다양한 Js 라이브러리가 있음
// 아래의 방법은 가장 무식한 방법.
obj1.value1 += 1;
console.log(obj1);
console.log(obj2);

// 직렬화 : 어떤 객체 메모리에 있는 리스트, 사전 등을 우리가 현재 프로세스 바깥이나 다른 서버로 
//          데이터를 보낼 수 있는 상태로 바꾸는 것. 순간이동이 가능한 상태로 바꿔서 ! 

// 재구성해서 문자열로 바꿔서 ~ 이를 다시 객체로 바꾸고 ..

const json_string = JSON.stringify(obj1) // 항상 동작하는 것 x 기본타입에는 동작
// 문자열로 바꿔서 전송 - > 전송했다가 다시 복원을 시킴
// 이는 ?
const obj3 = JSON.parse(json_string);
// 이렇게! 가장 무식한 파일 전송 
// 가장 원초적인 방법 . -> obj3는 깊은 복사가 된 것 


// 직렬화 -> 비직렬화 -> 같은 모양을 가진 새로운 변수가 생성
console.log(obj3);

