import { useReducer } from 'react';
/*
3. 하나의 상탯값에 numbers, colors 2개의 값을 담습니다.
	- numbers : 숫자 7개를 담은 배열. 
    초기값은 [0, 0, 0, 0, 0, 0, 0]
	
    - colors : 각 숫자의 글자색을 담은 배열. 
    초기값은 ["#1B62BF", "#1755A6", "#37A647", "#F29F05", "#F23838", "purple", "pink"]
 (useReducer만 사용)
*/
function reducer(prevState, action) {}

function SevenNumbers() {
  const [state, dispatch] = useReducer(reducer, {
    numbers: [0, 0, 0, 0, 0, 0, 0],
    colors: [
      '#1B62BF',
      '#1755A6',
      '#37A647',
      '#F29F05',
      '#F23838',
      'purple',
      'pink',
    ],
  });
  return (
    <div>
      <h2>7개의 숫자</h2>
    </div>
  );
}

export default SevenNumbers;
