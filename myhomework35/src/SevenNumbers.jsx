import { useReducer } from 'react';
/*
5. 버튼 3개
 - GENERATE_NUMBERS : 새로운 numbers를 랜덤하게 뽑아서 numbers에 적용
 - SHUFFLE_NUMBERS : 기존 numbers를 순서를 랜덤하게 섞습니다. 순서만 바꿀 뿐.
 - SHUFFLE_COLORS : 기존 colors의 순서를 랜덤하게 섞습니다. 순서만 바꿀 뿐.
*/
function reducer(prevState, action) {
  const { type } = action;
  if (type === 'GENERATE_NUMBERS') {
    let numList = [];
    for (let i = 1; i < 46; i++) {
      numList.push(i);
    }
    const generateNumber = numList
      .map((num_random) => ({
        num_random,
        value: Math.random(),
      }))
      .sort((obj_a, obj_b) => {
        return obj_a.value - obj_b.value;
      })
      .map(({ num_random }) => {
        return num_random;
      })
      .slice(0, 7);
    return { ...prevState, numbers: generateNumber };
  } else if (type === 'SHUFFLE_NUMBERS') {
    let shuffledNumbers = [];
    shuffledNumbers = prevState.numbers.sort(() => Math.random() - 0.5);
    return { ...prevState, numbers: shuffledNumbers };
  } else if (type === 'SHUFFLE_COLORS') {
    let shuffledColors = [];
    shuffledColors = prevState.colors.sort(() => Math.random() - 0.5);
    return { ...prevState, colors: shuffledColors };
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

  // dispatch 함수 따로 정의

  // const GENERATE_NUMBERS = () => {
  //   dispatch({ type: 'GENERATE_NUMBERS' });
  // };

  // const SHUFFLE_NUMBERS = () => {
  //   dispatch({ type: 'SHUFFLE_NUMBERS' });
  // };

  // const SHUFFLE_COLORS = () => {
  //   dispatch({ type: 'SHUFFLE_COLORS' });
  // };

  return (
    <div>
      <h2>7개의 숫자</h2>
      <div>
        <br />
        {state.numbers &&
          state.numbers.map((num, index) => {
            return (
              <div
                style={{
                  ...defaultStyle,
                  backgroundColor: state.colors[index],
                }}
              >
                {num}
              </div>
            );
          })}
        <hr />
        {/* dispatch 함수 따로 정의 없이, 화살표 함수로 바로 적용 */}
        <button onClick={() => dispatch({ type: 'GENERATE_NUMBERS' })}>
          GENERATE_NUMBERS
        </button>
      </div>
      <hr />

      <div>
        <button onClick={() => dispatch({ type: 'SHUFFLE_NUMBERS' })}>
          SHUFFLE NUMBERS
        </button>
        <br />
      </div>

      <hr />
      <div>
        <button onClick={() => dispatch({ type: 'SHUFFLE_COLORS' })}>
          SHUFFLE COLORS
        </button>
        <hr />
      </div>
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
