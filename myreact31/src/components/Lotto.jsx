import { useState } from 'react';

function makeLottoNumbers() {
  // shuffledNumber를 반환
  // 상탯값 정의

  // 1) 1~46까지 숫자를 array에 append(push)
  let numbers = [];
  for (let i = 1; i < 46; i++) {
    numbers.push(i);
  }

  // 2) 번호 섞기 - Math.random() 사용

  const shuffledNumber = numbers
    .map((num_random) => ({
      num_random,
      value: Math.random(),
    }))

    // 3) sort - 오름차순 기준으로 sort
    .sort((obj_a, obj_b) => {
      return obj_a.value - obj_b.value; // 난수를 생성해서 ? 그걸 통해서 섞어주는 거라서 이부분이 섞는 것
    })

    // 4) 다시 map -> 위에서 인자가 num_random/ value기 때문에 필요한 첫번째 인자만 빼서 map
    .map(({ num_random }) => {
      return num_random;
    })

    // 5) .slice 해서 우선 값을 7개를 빼냄
    .slice(0, 7)

    // 6) 이제 랜덤 값을 오름차순으로 빼기
    .sort((obj_a, obj_b) => {
      return obj_a - obj_b;
    });
  return shuffledNumber;
}

function LottoPredict() {
  const [number, setNumber] = useState([]);

  const clickButton = () => {
    setNumber(makeLottoNumbers);
  };

  // 함수명인 makeLottoNumbers이 반환하는 값을 setNumber()로 셋팅해준다.

  return (
    <div>
      <button onClick={clickButton}>예지</button>
      {number.map((num) => {
        return <div style={{ ...style, backgroundColor: 'red' }}>{num}</div>;
      })}
    </div>
  );
}

// style
const style = {
  width: '100px',
  height: '100px',
  borderRadius: '60px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  margin: '2rem',
  userSelect: 'none',
};

export default LottoPredict;
