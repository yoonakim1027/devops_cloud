// 파이썬의 장식자 문법과 비슷 
// 
// function base_10(fn) {
//     function wrap(x, y) {
//         return fn(x, y) + 10;
//     }
//     return wrap;
// }


// function mysum(x, y) {
//     return x + y;
// }

// mysum = base_10(base_10(mysum));

// console.log(mysum(1, 2));




// arrow function 버전으로 바꾸기 



// async function wrap1(x, y) {
//     //에러는?
//     try { // 한줄 읽어내고, 이줄에서 에러가 발생하면 에러 코드로 넘어가고 
//         function fn(x, y) {
//             return fn(x, y) + 10
//         };

//     } // 비동기지만, 동기적인 코드를 작성하는 것을 도와줌 
//     catch (error) {
//         console.error(error);
//     }

// }
// console.log(wrap1(1, 2));


/// arrow function
const base_10 = (fn) => (x, y) => fn(x, y) + 10;

// 이 코드를 풀면?
// function base_10(fn) {
//     function wrap(x, y) {
//         return fn(x, y) + 10;
//     }
//     return wrap;
// } -> 이거랑 같음


// wrap 만들자 마자 리턴 -> 

