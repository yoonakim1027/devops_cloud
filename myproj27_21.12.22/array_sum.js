
// reduce((첫번째 인자는 초기값, 두번째 값은 계속 연산될 값 ))
Array.prototype.sum = function () {
    this.reduce((acc, element) => {
        return acc + element;

    }, 0); // 합을 구할 것이니까 초기값은 0
};

// this 가 동작하려면 꼭!! function을 써야 한다
// prototype을 쓰는 것은 자바 스크립트만의 특성 

// 기존에 존재하는 클래스에 대해, 확장시킬 수 있음 
const result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].sum();
console.log(result);


/*
reduce는 array(배열)에 있는 함수

*/