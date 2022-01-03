import { useState } from "react";

/*1. Counter 컴포넌트 기본 모양을 만듭니다. (오른쪽 첫번째 스샷 참고) 
- App.js에서 Counter 컴포넌트를 렌더링합니다. (V)
2. +/- 버튼을 추가하고, click 이벤트 핸들러를 통해 setValue에 직접적으로 값을 넘겨 상탯값을 변경합니다. (no 함수)
(v)
3, +/- 버튼에 대한 이벤트 핸들러에서 setValue에 함수를 넘겨 상탯값을 변경합니다. (value를 참조 X)
(v)
4. green/blue/red 버튼을 추가하고, click 이벤트 핸들러를 통해 setColor에 직접적으로 값을 넘겨 상탯값을 변경합니다. (no 함수)
(v)

5. green/blue/red 버튼에 대한 이벤트 핸들러에서 setColor에 함수를 넘겨 상탯값을 변경합니다. ( color를 참조 X)
-- 4번까지의 과정을 주석처리 해야 가능 
*/

function Counter3() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  // 2. 함수 없이 구현 -> 이게 직접 값을 변경해서 넘겨주는 것
  // 증가
  //   const handlePlus = () => {
  //     setValue(value + 1);
  //   };

  // 감소
  //   const handleMinus = () => {
  //     setValue(value - 1);
  //   };

  // red
  //   const handleColorRed = () => {
  //     setColor("red");
  //   };

  // green
  //   const handleColorGreen = () => {
  //     setColor("green");
  //   };

  // blue
  //   const handleColorBlue = () => {
  //     setColor("blue");
  //   };

  // 새로운 값을 리턴 -> 원래의 값(뭔가를)을 변경 X
  // 5번 //
  // 증가 버튼
  const handlePlus = () => {
    setValue((prevValue) => prevValue + 1);
  }; // 직전상탯값

  // 감소 버튼
  const handleMinus = () => {
    setValue((prevValue) => prevValue - 1);
  };

  // 색은 이전값이 있지만? 어처피 그냥 색변환이라서 참조하지 않아도 됨  -> 항상 모든 것은 절댓값. 읽기 전용
  // setter(함수) : 이 함수에게 기대하는 것은? 새로운 상탯값을 반환해주는 것(return)
  // 값을 직접 할당하는 것은 우리가 하는 것이 아님!
  // () => {} 이게 함수임 !

  // red
  const handleColorRed = () => {
    setColor(() => "red");
  }; // 직전값 있는데(아까 useState로 'red'로 정했음), 근데? 안쓰는 거라 안받음
  // -> 안쓰면 안받아도 오류가 안남 ! 참조할필요가 없어서 (파이썬은 오류남)

  // green
  const handleColorGreen = () => {
    setColor(() => "green");
  };

  // blue
  const handleColorBlue = () => {
    setColor(() => "blue");
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
