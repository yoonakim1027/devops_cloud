import { useState } from "react";

/*

1. (+/- 버튼의 이벤트 핸들러에서만) reducer 함수를 선언하고, action, prevState 2개의 인자를 받도록 하고
 action, prevState 기반에서 /  새로운 상탯값을 반환토록 구현해주세요.

2. (green/blue/red 버튼의 이벤트 핸들러에서만) reducer 함수에서 새로운 상탯값을 반환토록 구현해주세요. 
  // reducer 함수를 호출하여, 새로운 상탯값을 계산해냅니다.
*/
// setter(prevState => reducer(action, prevState))
// 리턴값은 객체로 반환 !
function reducer(action, prevState) {
  const { type, amount, color } = action; // 객체

  // 객체니까 리턴도 객체로 받아야 함!!
  // -> 이름을 통일 시키기!
  // 증감
  if (type === "COUNT") {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === "CHANGE_COLOR") {
    return { ...prevState, color: color };
  }
  // 버그 !
  return prevState;
}

function Counter3() {
  const [state, setState] = useState({ value: 0, color: "red" }); // 초깃값을 {오브젝트: 객체}로 지정했기 때문에?
  const { value, color } = state; // -> 객체로 받아야 한다.

  // 증가 버튼
  const handlePlus = () => {
    const action = { type: "COUNT", amount: 1 };
    setState((prevState) => {
      return reducer(action, prevState);
    });
    // 새로운 상탯값이 reducer를 통해서 생성되고, 이게 setState로 적용되는 것
  };

  // 감소 버튼
  const handleMinus = () => {
    const action = { type: "COUNT", amount: -1 }; // 음수 ...
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  // red
  const handleColorRed = () => {
    const action = { type: "CHANGE_COLOR", color: "red" };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  // green
  const handleColorGreen = () => {
    const action = { type: "CHANGE_COLOR", color: "green" };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };
  // blue
  const handleColorBlue = () => {
    const action = { type: "CHANGE_COLOR", color: "blue" };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  return (
    <div>
      <h2>Counter3</h2>

      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <br />
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>

      <br />
      <button onClick={handleColorRed}>red</button>
      <button onClick={handleColorGreen}>green</button>
      <button onClick={handleColorBlue}>blue</button>
      <hr />
      {JSON.stringify(state)}
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
