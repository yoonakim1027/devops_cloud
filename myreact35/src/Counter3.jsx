import { useState, useReducer } from "react";

/*
상탯값 정의를 useState가 아니라 useReducer로 변경
*/
// setter(prevState => reducer(action, prevState))
// 리턴값은 객체로 반환 !
function reducer(prevState, action) {
  const { type, amount, color } = action; // 객체
  // 증감
  if (type === "COUNT") {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === "CHANGE_COLOR") {
    return { ...prevState, color: color };
  }
  // 버그 !
  return prevState;
}
// useReducer(reducer, 초기값)

function Counter3() {
  const [state, dispatch] = useReducer(reducer, { value: 0, color: "red" });
  //const [state, setState] = useState({ value: 0, color: "red" }); // 초깃값을 {오브젝트: 객체}로 지정했기 때문에?
  //const { value, color } = state; // -> 객체로 받아야 한다.

  // 증가 버튼
  const handlePlus = () => {
    // const action = { type: "COUNT", amount: 1 };
    // setState((prevState) => {
    //   return reducer(action, prevState);
    // });
    dispatch({ type: "COUNT", amount: 1 });
  };

  // 감소 버튼
  const handleMinus = () => {
    // const action = { type: "COUNT", amount: -1 }; // 음수 ...
    // setState((prevState) => {
    //   return reducer(action, prevState);
    // });
    dispatch({ type: "COUNT", amount: -1 });
  };

  // red
  const handleColorRed = () => {
    // const action = { type: "CHANGE_COLOR", color: "red" };
    // setState((prevState) => {
    //   return reducer(action, prevState);
    // });
    dispatch({ type: "CHANGE_COLOR", color: "red" });
  };

  // green
  const handleColorGreen = () => {
    // const action = { type: "CHANGE_COLOR", color: "green" };
    // setState((prevState) => {
    //   return reducer(action, prevState);
    // });
    dispatch({ type: "CHANGE_COLOR", color: "green" });
  };
  // blue
  const handleColorBlue = () => {
    // const action = { type: "CHANGE_COLOR", color: "blue" };
    // setState((prevState) => {
    //   return reducer(action, prevState);
    // });
    dispatch({ type: "CHANGE_COLOR", color: "blue" });
  };

  return (
    <div>
      <h2>Counter3</h2>

      <div style={{ ...defaultStyle, backgroundColor: state.color }}>
        {state.value}
      </div>
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
