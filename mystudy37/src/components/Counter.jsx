import './Counter.css';
import { useState, useReducer } from 'react';
import { type } from '@testing-library/user-event/dist/type';

// 1. useState로 handleClick(왼쪽 클릭), handleRightClick(오른쪽 클릭)
// 2. useRecucer로 handleClick(왼쪽 클릭), handleRightClick(오른쪽 클릭)

// reducer에서 사용할 action types 정의
const ACTION_TYPES = {
  HANDLECLICK: 'HANDLECLICK',
  HANDLERIGHTCLICK: 'HANDLERIGHTCLICK',
};

// reducer 함수 정의
function reducer(prevState, action) {
  const { type, amount } = action; // type정의와 amount로 동적으로 값을 받기위해 인자로 받음
  if (type === ACTION_TYPES.HANDLECLICK) {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === ACTION_TYPES.HANDLERIGHTCLICK) {
    return { ...prevState, value: prevState.value - amount };
  }
}

function Counter() {
  // 상탯값 지정 => 숫자라서 초깃값 0으로 지정
  const [value, setValue] = useState(0);
  // 초깃값(value) : 1
  const [state, dispatch] = useReducer(reducer, { value: 0 });

  // useState : 왼쪽 클릭
  const handleClick = () => {
    setValue((prevValue) => prevValue + 1);
  };

  // useState : 오른쪽 클릭 -> 오른쪽 클릭시에 창뜨는것 방지
  const handleRightClick = (e) => {
    e.preventDefault();
    setValue((prevValue) => prevValue - 1);
  };

  // useReducer : 왼쪽 클릭
  const reducerHandleClick = () => {
    dispatch({ type: ACTION_TYPES.HANDLECLICK, amount: 1 });
  };
  // useReducer : 오른쪽 클릭
  const reducerHandleRightClick = (e) => {
    e.preventDefault();
    dispatch({ type: ACTION_TYPES.HANDLERIGHTCLICK, amount: 1 });
  };

  return (
    <>
      <h2>Counter : useState</h2>
      <div
        className="counter"
        style={{
          backgroundColor: 'blue',
        }}
        onClick={handleClick}
        onContextMenu={handleRightClick}
      >
        {value}
      </div>
      <hr />
      <h2>Counter : useReducer</h2>
      <div
        className="counter"
        style={{
          backgroundColor: 'red',
        }}
        onClick={reducerHandleClick}
        onContextMenu={reducerHandleRightClick}
      >
        {state.value}
      </div>
      <hr />
    </>
  );
}

export default Counter;
