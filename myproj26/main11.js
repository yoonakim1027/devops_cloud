// 파이썬의 import와 비슷
const fs = require("fs");

// 자바스크립는 기본적으로 비동기 (순서 X )
// .은 현재경로
// err -> 에러 

// 에러 유무 판단 
fs.readdir("c:/Dev", function (err, files) {
    if (err) { // 없으면 에러메시지를 출력하라 
        console.error(err);

    }
    //에러가 없다면 디렉토리 경로를 읽음(정상적으로 읽어옴 -> 파일내용을 출력 )
    else {
        console.log(files);
    }
})


