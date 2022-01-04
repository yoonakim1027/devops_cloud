// useState 버전

import Circle from 'Circle';
import { useState } from 'react';
import { shuffle_array, zip } from 'utils';

const INITIAL_STATE = {
  numbers: [0, 0, 0, 0, 0, 0, 0],
  colors: [
    '#1B62BF',
    '#1755A6',
    '#37A647',
    '#F29F05',
    '#F23838',
    'purple',
    'pink',
  ],
};

const get_lotto_numbers = () =>
  [...Array(45).keys()]
    .map((index) => index + 1)
    .sort(() => Math.random() - Math.random())
    .slice(0, 7)
    .sort((number1, number2) => number1 - number2);

function SevenNumbers1({ title }) {
  const [state, setState] = useState(INITIAL_STATE);

  const generateNumbers = () => {
    // 하나의 배열에서 7개의 랜덤수를 생성하는 함수
    setState((prevState) => ({
      ...prevState,
      numbers: get_lotto_numbers(),
    }));
  };

  const shuffleNumbers = () => {
    setState((prevState) => ({
      ...prevState,
      numbers: shuffle_array(prevState.numbers),
    }));
  };

  const shuffleColors = () => {
    setState((prevState) => ({
      ...prevState,
      colors: shuffle_array(prevState.colors),
    }));
  };

  // 이벤트 처리 -> if 사용 -> 클릭했을 때 들어온 인덱스가 같으면 컬러를 변경
  // 맵으로 뽑는 인덱스가 받아온 인덱스와 같다면
  const changeCirleColor = (circleIndex) => {
    setState((prevState) => ({
      ...prevState,
      colors: prevState.colors.map((color, index) => {
        if (index === circleIndex) {
          return (color = `#${Math.round(Math.random() * 0xffffff).toString(
            16,
          )}`);
        }
        return color;
      }),
    }));
  };

  // const removeCirle = (circleIndex) => {};

  return (
    <div>
      {title && <h2>{title}</h2>}
      {zip(state.numbers, state.colors).map(([number, color], index) => (
        <Circle // 특정 circle을 클릭했을때 동작하는 밑의 함수들
          number={number}
          backgroundColor={color}
          onClick={() => changeCirleColor(index)}
          onContextMenu={(e) => {
            e.preventDefault();
            console.log(`right clicked : ${index}`);
          }}
        />
      ))}
      <hr />
      <button onClick={generateNumbers}>GENERATE_NUMBERS</button>
      <button onClick={shuffleNumbers}>SHUFFLE_NUMBERS</button>
      <button onClick={shuffleColors}>SHUFFLE_COLORS</button>
      <hr />
      <pre>{JSON.stringify(state, null, 4)}</pre>
    </div>
  );
}

export default SevenNumbers1;
