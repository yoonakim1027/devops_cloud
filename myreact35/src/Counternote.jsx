import { useState } from "react";

/*
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

  const handleColorRed = () => {
    const action = { type: "CHANGE_COLOR", color: "red" };
    setColor((prevColor) => {
      return reducer(action, prevColor);
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
