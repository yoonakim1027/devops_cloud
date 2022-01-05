import { useState } from 'react';
import './Counter.css';

function Counter() {
  const [value, setValue] = useState(0);

  const handleClick = () => {
    setValue(value + 1);
  };

  return (
    <div
      className="counter"
      style={{
        backgroundColor: 'red',
      }}
      onClick={handleClick}
    >
      {value}
    </div>
  );
}

export default Counter;
