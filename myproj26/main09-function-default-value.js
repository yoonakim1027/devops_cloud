// function hello(name, age) {
//     console.log(`안녕. 나는 ${name}이야. ${age}살이지.`);
// }

// hello("Tom");
// hello("steve");
// hello("jone");

// // age를 지정하지 않아서~ 


// // const get_default_value = () => 10;
// // const get_default_value = () => {
// //     return 10;
// // }


const get_default_value = () => {
    console.log("get_defalut_value() 함수 호출 ");
    return 10;
}

function hello(name, age = get_default_value()) {
    console.log(`안녕. 나는 ${name}이야, ${age}살이지.`);
}

hello("Tom");

hello("steve");

hello("yoona");

// 함수는 defalut 값이 필요할 때에만 호출!
// defalut 값이 있으면 호출되지 않는다~
// 나이값이나 이름 값이 들어가 있다면 호출되지 않는다.
// js만의 특징

// 자바스크립트에서는 실제 디폴트 값이 필요한 시점에 호출! 
