//Array
const [name] = ['Tom', 10, "seoul"];

// js세상에선 좌항 우항의 갯수가 달라도 에러가 발생하지 않음
// 이렇게 하면? 'Tom"만 name 변수에 저장이됨


const [, age,] = ['Tom', 10, "Seoul"]

// 이렇게 양옆에 변수명을 비어도됨. 
// 앞부분의 인덱스만 맞춰주면 됨
// [,age] 이렇게만 해도 됨~ 


const [name, age, region, height] = ["Tom", 10, "Seoul"];
// 좌항과 우항의 갯수가 다름
// 좌항이 한 개 더 많음
// 그러면 에러가 발생하는 것이 아니라, height 에는 undefined가 들어감.(값이 없음)

const [name, age, region, height = 140] = ["Tom", 10, "Seoul"];
// height 값은 있을 수도 있고, 없을 수도 있다.
// 그러면? height = 140 이렇게 defalut값을 지정할 수 있음. 
// 값 할당에 실패 했을 때 적용되는 디폴트 값 
// array에 해당하는 값이 없을때, height에는 140이라는 디폴트 값이 저장이 됨 

// 디폴트 값은 파이썬과 다른 측면이 있음

function get_default_height() {
    console.log("get_default_height 함수를 호출했습니다.");
    return 140;
}

// 함수() 호출까지 해야함~ 
const [name, age, region, height = get_default_height()] = ["Tom", 10, "Seoul", 150];

const [name, age, region, height = get_default_height()] = ["Tom", 10, "Seoul"];

// 디폴트 값을 함수 호출로 지정 : 디폴트 값이 필요한 시점에 함수가 호출된다.
// 파이썬과 다름.
// 디폴트 값이라고 쓴다고 해서?
// 각 함수가 호출되서 값이 140으로 되는것이 아니라,
// undefined 일때, 뒤늦게 호출이 되서 할당이 된다 (js만의 특성)
