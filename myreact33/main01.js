const numbers = [1, 2, 3, 4, 5];

const new_numbers = numbers.filter((num) => {
  return num % 2 == 0; 결과는 참 혹은 거짓을 반환한다 
  filter가 첫번째 함수에 기대하는 것은 참 혹은 거짓 
  참 혹은 거짓...각각의 항목...true
  
});

console.log(new_numbers);
어떤 항목을 탈락, 포함 시킬지 필터를 통해 결정
-. 새로운 배열 형성 
인자로 받는 것은 그 값 
값을 받아서 탈락 여부 -> true, False 

const new_numbers2 = numbers.filter((num) => {
  return num % 2 == 1;
});

console.log(new_numbers2);

// 테스트를 통과한 요소로 이루어진 새로운 배열. 어떤 요소도 테스트를 통과하지 못했으면 빈 배열을 반환합니다.

//  주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환

