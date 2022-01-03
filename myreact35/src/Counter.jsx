import { useState } from "react";
/*
- 마이너스 버튼을 만드시고 클릭 시 마다 -1
- 상탯값 변경 시에는 함수로 구현

*/

function Counter({ initialValue }) {
  // 상탯값 정의
  const [value, setValue] = useState(initialValue);

  // 상탯값 변경하는 함수들
  const handlePlus = () => {
    // setValue(value + 1); // 비동기 세상
    // setValue(value + 2);

    setValue((prevValue) => prevValue + 1);
  };
  const handleMinus = () => {
    // setValue(value + 1); // 비동기 세상
    // setValue(value + 2);

    setValue((prevValue) => (prevValue -= 1));
  };

  // 보여지는 것들을 정의
  return (
    <div>
      <h2>Counter</h2>
      {value}
      <hr />
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>
    </div>
  );
}

export default Counter;
