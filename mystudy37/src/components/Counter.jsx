import './Counter.css';
import { useState } from 'react';

// 1. useState로 handleClick(왼쪽 클릭), handleRightClick(오른쪽 클릭)

function Counter() {
  // 상탯값 지정 => 숫자라서 초깃값 0으로 지정
  const [value, setValue] = useState(0);

  //왼쪽 클릭
  const handleClick = () => {
    setValue((prevValue) => prevValue + 1);
  };

  // 오른쪽 클릭 -> 오른쪽 클릭시에 창뜨는것 방지
  const handleRightClick = (e) => {
    e.preventDefault();
    setValue((prevValue) => prevValue - 1);
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
    </>
  );
}

export default Counter;
