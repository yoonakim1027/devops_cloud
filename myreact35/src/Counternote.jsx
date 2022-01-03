import { useState } from "react";

/*1. Counter 컴포넌트 기본 모양을 만듭니다. (오른쪽 첫번째 스샷 참고) 
- App.js에서 Counter 컴포넌트를 렌더링합니다. (V)
2. +/- 버튼을 추가하고, click 이벤트 핸들러를 통해 setValue에 직접적으로 값을 넘겨 상탯값을 변경합니다. (no 함수)
(v)

3, +/- 버튼에 대한 이벤트 핸들러에서 setValue에 함수를 넘겨 상탯값을 변경합니다. (value를 참조 X)
4. green/blue/red 버튼을 추가하고, click 이벤트 핸들러를 통해 setColor에 직접적으로 값을 넘겨 상탯값을 변경합니다. (no 함수)

*/

//3. 함수 사용
function reducer(action, prevState) {
  const { type, amount } = action;
  if (type === "PLUS") {
    return prevState + amount;
  } else if (type === "MINUS") {
    return prevState - amount;
  }
  // 버그 !!!
  return prevState;
}

function Counter3() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  // 2. 함수 없이 구현
  //   const handlePlus = () => {
  //     setValue(value + 1);
  //   };

  //   const handleMinus = () => {
  //     setValue(value - 1);
  //   };

  // 증가 버튼
  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setValue((prevValue) => {
      // dispatch 함수를 호출하여, 새로운 상탯값을 계산해냅니다.
      return reducer(action, prevValue);
    });
  };

  // 감소 버튼
  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  return (
    <div>
      <h2>Counter3</h2>

      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>
    </div>
  );
}

const defaultStyle = {
  width: "100px",
  height: "100px",
  borderRadius: "50px",
  lineHeight: "100px",
  textAlign: "center",
  display: "inline-block",
  fontSize: "3rem",
  userSelect: "none",
};

export default Counter3;
