import { useReducer } from 'react';
/*
5. 버튼 3개
 - GENERATE_NUMBERS : 새로운 numbers를 랜덤하게 뽑아서 numbers에 적용
 - SHUFFLE_NUMBERS : 기존 numbers를 순서를 랜덤하게 섞습니다. 순서만 바꿀 뿐.
 - SHUFFLE_COLORS : 기존 colors의 순서를 랜덤하게 섞습니다. 순서만 바꿀 뿐.
*/
function reducer(prevState, action) {
  const { type, color } = action;
  if (type === 'GENERATE_NUMBERS') {
    let numList = [];
    for (let i = 1; i < 46; i++) {
      numList.push(i);
    }
    const shuffledNumber = numList
      .map((num_random) => ({
        num_random,
        value: Math.random(),
      }))
      .sort((obj_a, obj_b) => {
        return obj_a.value - obj_b.value; // 난수를 생성해서 ? 그걸 통해서 섞어주는 거라서 이부분이 섞는 것
      })
      .map(({ num_random }) => {
        return num_random;
      })
      .slice(0, 7);
    return { number: shuffledNumber };
  } else if (type === 'COLOR') {
    return { prevState, color };
  }
}

function SevenNumbers() {
  const [state, dispatch] = useReducer(reducer, {
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
  });

  const GENERATE_NUMBERS = () => {
    dispatch({ type: 'GENERATE_NUMBERS' });
  };

  return (
    <div>
      <h2>7개의 숫자</h2>
      <div>
        <button onClick={GENERATE_NUMBERS}>GENERATE_NUMBERS</button>
        <br />
        {state.number &&
          state.number.map((num) => {
            return (
              <div style={{ ...defaultStyle, backgroundColor: 'red' }}>
                {num}
              </div>
            );
          })}
      </div>

      <button>SHUFFLE NUMBERS</button>
      <button>SHUFFLE COLORS</button>
      <hr />
      {JSON.stringify(state)}
    </div>
  );
}

const defaultStyle = {
  width: '100px',
  height: '100px',
  borderRadius: '100px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  userSelect: 'none',
};

export default SevenNumbers;
