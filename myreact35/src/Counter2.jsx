import { useState } from "react";

// { type: "PLUS", amount: 1 }
// { type: "MINUS", amount: 1 }

/*
1. 상탯값을 정의
2. Counter2의 기본 모양을 jsx로 구성
3. handlePlus, handleMinus 구현
- setValue를 호출 시에 함수 인자를 제공
4. dispatch 함수를 구현
5. dispatch 함수를 활용

dispatch 함수를 호출 시에, 새로운 상탯값을 계산해서 호출
계산에 필요한 action, prevState 두개 값으로 새로운 상탯값 계산
인자에 기반해서 계산
인자 의외에 다른 어떤 값을 참조 X (참조해서도 안되는 순수 함수)
-> dispatch는 무조건 순수함수로만 해야 함
- dispatch는 항상 같은 값을 반환해야 한다 
=> 다른 값을 반환해서는 안된다
= 항상 순수 함수로써 구현이 되어야만 한다!
즉 같은 값의 인자가 주어지면 
-> 항상 같은 값을 리턴을 해야만 하고
-> 인자 외의 다른 어떤 값, 어떤 통신을 해서도 안된다
(순수함수이기 때문에! 이렇게 해야지만 리액트 패러다임에 맞게 코드를 가져갈 수 있다.)


--------------- 오후에는
1. 새로운 상탯값 color, setColor를 정의
- 초기값 : "red"

2. 3개의 버튼 "색상 변경"

- 1번 버튼 : 녹색으로 변경 => {action: "CHANGE_COLOR", color:"green"}
- 2번 버튼 "blue" 상호 전환 => {action: "CHANGE_COLOR", color:"blue"}
- 3번 버튼 : "red" => {action: "CHANGE_COLOR", color:"red"}
(현재는 값만 변경하는 dispatch 함수)

3. 새로운 dispatch 함수인 dispatch_color 함수를 구현 

*/

function dispatch(action, prevState) {
  const { type, amount } = action;
  if (type === "PLUS") {
    return prevState + amount;
  } else if (type === "MINUS") {
    return prevState - amount;
  }
  // 버그 !!!
  return prevState;
}
// 함수 두개가 필요!
//   const newState = action;
//   if ()
//   return newState

function reducer(action, prevColor) {
  const { type, color } = action;
  if (type === "red") {
    return (prevColor = color);
  } else if (type === "green") {
    return (prevColor = color);
  } else {
    return (prevColor = color);
  }
  // 버그
  return prevColor;
}

function Counter2() {
  // TODO: color와 value
  // 지금의 초기값 : 0 -> 하나의 상탯값으로 두개를 처리
  // 오후의 초기값은 : {오브젝트로 value : 0, color : "red"}

  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  // 증가 버튼
  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setValue((prevValue) => {
      // dispatch 함수를 호출하여, 새로운 상탯값을 계산해냅니다.
      return dispatch(action, prevValue);
    });
  };

  // 감소 버튼
  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setValue((prevValue) => {
      return dispatch(action, prevValue);
    });
  };

  // 색 변경 버튼
  const handleColorRed = () => {
    const action = { type: "CHANGE_COLOR", color: "red" };
    setColor((prevColor) => {
      return reducer(action, prevColor);
    });
  };
  const handleColorGreen = () => {
    const action = { type: "CHANGE_COLOR", color: "green" };
    setColor((prevColor) => {
      return reducer(action, prevColor);
    });
  };

  const handleColorBlue = () => {
    const action = { type: "CHANGE_COLOR", color: "blue" };
    setColor((prevColor) => {
      return reducer(action, prevColor);
    });
  };

  return (
    <div>
      <h2>Counter2</h2>

      <hr />
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
      <p></p>
      <button onClick={handleColorRed}>버튼1</button>
      <button onClick={handleColorGreen}>버튼2</button>
      <button onClick={handleColorBlue}>버튼3</button>
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

export default Counter2;
