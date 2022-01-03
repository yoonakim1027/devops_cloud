import { useState } from "react";

/*
6. value/color 2개의 상탯값을 하나의 상탯값으로 처리합니다.
  const [state, setState] = useState({ value: 0, color: "red" });
  
  value/setValue/color/setColor를 참조하는 코드를 
  state/setState를 참조토록 모두 변경해주세요.
  // 새로운 값을 리턴 -> 원래의 값(뭔가를)을 변경 X
  */

function Counter3() {
  const [state, setState] = useState({ value: 0, color: "red" }); // 초깃값을 {오브젝트: 객체}로 지정했기 때문에?
  const { value, color } = state; // -> 객체로 받아야 한다.

  // setState 에는 "함수"를 넘겨야함 ! -> 인자로 직전값인 prevState가 넘어온다

  // 증가 버튼
  const handlePlus = () => {
    const newState = (prevState) => {
      return {
        ...prevState, // unpacking -> 전체를 다 풀어와서~
        value: prevState.value + 1, // 그 중 바꿀값의 키 :
      };
    };
    setState(newState);
  };

  // 감소 버튼
  const handleMinus = () => {
    const newState = (prevState) => {
      return {
        ...prevState,
        value: prevState.value - 1,
      };
    };
    setState(newState);
  };

  // red
  const handleColorRed = () => {
    const newState = (prevState) => {
      return {
        ...prevState,
        color: "red",
      };
    };
    setState(newState);
  };

  // green
  const handleColorGreen = () => {
    const newState = (prevState) => {
      return {
        ...prevState,
        color: "green",
      };
    };
    setState(newState);
  };

  // blue
  const handleColorBlue = () => {
    const newState = (prevState) => {
      return {
        ...prevState,
        color: "blue",
      };
    };
    setState(newState);
  };

  return (
    <div>
      <h2>Counter3</h2>

      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <br />
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>

      <br />
      <button onClick={handleColorRed}>Red</button>
      <button onClick={handleColorGreen}>Green</button>
      <button onClick={handleColorBlue}>Blue</button>
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
