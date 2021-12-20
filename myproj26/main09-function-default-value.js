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