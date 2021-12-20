const mysum2 = (x, y) => { x, y };
console.log(mysum2(1, 2));

const mysum3 = (x, y) => {
    return { x, y }
};
console.log(mysum3(1, 2));

// 중괄호는 매 시작을 의미 
// 항상 중괄호로 시작을 해줘야 함 


// 반환할 형태를 객체로 하고 싶다면? 소괄호로 묶어주기 
// 소괄호 -> 우선순위 연산자 
const mysum4 = (x, y) => ({ x, y });
console.log(mysum4(1, 2));