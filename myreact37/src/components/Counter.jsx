import { useStae } from 'react';
import './Counter.css';

function Counter() {
  const [value, setValue] = useStae(0);
  return (
    <div
      className="counter"
      style={{
        backgroundColor: 'red',
      }}
    >
      {value}
    </div>
  );
}

export default Counter;
