import { useState, useReducer } from 'react';
import './Counter.css';
// reducer에는 필요한 인자가 2개
// 첫번째 인자는 직전값, 두번째 인자는 여기에 적용할 action

const ACTION_TYPES = {
  HANDLECLICK: 'HANDELCLICK',
  HANDLERIGHTCLICK: 'HANDLERIGHTCLICK',
};

function reducer(prevState, action) {
  //reducer는 type 정의가 필수임!
  const { type, amount } = action;
  if (type === ACTION_TYPES.HANDLECLICK) {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === ACTION_TYPES.HANDLERIGHTCLICK) {
    return { ...prevState, value: prevState.value - amount };
  } // 객체 접근을 위해 .value 로 값에 접근해야 함
}

function Counter() {
  const [value, setValue] = useState(0);
  const [state, dispatch] = useReducer(reducer, { value: 0 }); // reducer, 초기상탯값

  //useState
  const handleClick = () => {
    setValue((prevValue) => prevValue + 1);
  };

  const handleRightClick = (e) => {
    e.preventDefault();
    setValue((prevValue) => prevValue - 1);
  };

  //useReducer
  const reduceHandleClick = () => {
    dispatch({ type: ACTION_TYPES.HANDLECLICK, amount: 1 }); // amount 값 추가
  };

  const reduceHandleRightClick = (e) => {
    e.preventDefault();
    dispatch({ type: ACTION_TYPES.HANDLERIGHTCLICK, amount: 1 });
  };

  return (
    <>
      <h2> Counter : useState</h2>
      <div
        className="counter"
        style={{
          backgroundColor: 'red',
        }}
        onClick={handleClick}
        onContextMenu={handleRightClick}
      >
        {value}
      </div>
      <hr />
      <h2> Counter : useReducer</h2>
      <div
        className="counter"
        style={{
          backgroundColor: 'red',
        }}
        onClick={reduceHandleClick}
        onContextMenu={reduceHandleRightClick}
      >
        {state.value}
      </div>
      <hr />
    </>
  );
}

export default Counter;
