// 파이썬의 import와 비슷
const fs = require("fs");

// 자바스크립는 기본적으로 비동기 (순서 X )
// .은 현재경로
// err -> 에러 

// // 에러 유무 판단 1번 : callback
// fs.readdir("c:/Dev", function (err, files) {
//     if (err) { // 없으면 에러메시지를 출력하라 
//         console.error(err);

//     }
//     //에러가 없다면 디렉토리 경로를 읽음(정상적으로 읽어옴 -> 파일내용을 출력 )
//     else {
//         console.log(files);
//     }
// })

// // 콜백을 했기 때문에 함수 지정이 멈춰있는 것이 아니라
// // 파일이 이 경로내에서 디렉토리를 읽어서 실행이되어야 위의 함수가 실행되는 것 
// // 이게 비동기 -> Async 
// console.log("ENDED");



/// 에러 유무 판단 2번 : Promises (이 방식이 주로 사용됨 )

// const fs = require("fs");
// const fsPromises = fs.promises;

// fsPromises.readdir("c:/Dev")
//     .then(files =>console.log("loaded:", files))
//     .catch(error => console.error(error));
    
//     // 약속 -> 위의 지정한 함수(readdir)가 정상적으로 동작했을때 나오는 함수 
//     // .then() : 정상 동작 시에 ?


// console.log("ENDED");


/// 에러 유무 판단 3번
// await는 promise 문법에 대한 축약
// await는 기다리는 것
// 기다려서, 밑에 코드가 디렉토리를 반환하는 것을 기다림 
async function main() {
    //에러는?
    try { // 한줄 읽어내고, 이줄에서 에러가 발생하면 에러 코드로 넘어가고 
        const files = await fsPromises.readdir("c:/Dev33");
        console.log("loaded:", files);

    } // 비동기지만, 동기적인 코드를 작성하는 것을 도와줌 
    catch(error) {
        console.error(error);
    }    

}

main(); // 함수 다시 호출 
// 꼭 async await 
// await는 항상 async 함수에서만 동작한다. 

