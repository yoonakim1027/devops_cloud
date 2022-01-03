import { useState, useReducer } from "react";

/*
상탯값 정의를 useState가 아니라 useReducer로 변경
*/
// setter(prevState => reducer(action, prevState))

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

  // 증가 버튼
  const handlePlus = () => {
    dispatch({ type: "COUNT", amount: 1 });
  };

  // 감소 버튼
  const handleMinus = () => {
    dispatch({ type: "COUNT", amount: -1 });
  };

  // red
  const handleColorRed = () => {
    dispatch({ type: "CHANGE_COLOR", color: "red" });
  };

  // green
  const handleColorGreen = () => {
    dispatch({ type: "CHANGE_COLOR", color: "green" });
  };
  // blue
  const handleColorBlue = () => {
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
