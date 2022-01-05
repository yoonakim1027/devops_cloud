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

  // 클릭한 circle만 색 변경
  // 바로 할당 없이 바로 return
  const changeCirleColor = (circleIndex) => {
    setState((prevState) => ({
      ...prevState,
      colors: prevState.colors.map((color, index) => {
        if (index === circleIndex) {
          return `#${Math.round(Math.random() * 0xffffff).toString(16)}`;
        }
        return color;
      }),
    }));
  };
  //우클릭했을때는 => numbers와 colors를 제거 -> filter를 사용해서 해당되는 인덱스만 제거
  //우클릭 시에 클릭한 Circle만 제거 (numbers/colors 배열의 filter 사용)
  // 조건에 대한 값이 True면 남고, False면 안남음

  // 반환하는 인수를 사용하지 않기때문에 언더바_ 로 사용하지 않겠다고 명시

  const removeCirle = (circleIndex) => {
    setState((prevState) => ({
      ...prevState,
      numbers: prevState.numbers.filter((_, index) => index !== circleIndex),
      colors: prevState.colors.filter((_, index) => index !== circleIndex),
    }));
  };
  // filter에서 === -> 같은 것만 filtering
  // filter에서 !== -> 다른 것만 찾게 되니까? 같은 것은 filtering이 안된다.
  // 그렇기 때문에 filter가 된 결과는 ? 다른 것들만 남은 배열

  return (
    <div>
      {title && <h2>{title}</h2>}
      {zip(state.numbers, state.colors).map(([number, color], index) => (
        <Circle // 특정 circle을 클릭했을때 동작하는 밑의 함수들
          number={number}
          backgroundColor={color}
          onClick={() => {
            console.log(`clicked : ${index}`);
            changeCirleColor(index);
          }}
          onContextMenu={(e) => {
            e.preventDefault();
            removeCirle(index);
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
