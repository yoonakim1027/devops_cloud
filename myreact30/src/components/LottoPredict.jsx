import { useState } from 'react';
import { Button, Tooltip, List, Avatar } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import { DollarCircleOutlined } from '@ant-design/icons';

// 로또 번호 예측
// 로또 번호는 1~45, 보너스번호 포함 6개

function LottoPrecict() {
  const [numList, setNumberList] = useState([]);

  //예지 버튼을 눌렀을 때 구현
  const handleClick = (e) => {
    console.group('handleClick');

    console.log('로또번호를 출력합니다.');

    let number = [];
    for (let i = 1; i < 46; i++) {
      number.push(i);
    }
    // 이 번호를 섞어줄 함수
    const shuffledNumber = number
      .map((number_random) => ({
        number_random,
        value: Math.random(),
      }))
      .sort((obj_a, obj_b) => {
        return obj_a.value - obj_b.value;
      })
      .map(({ number_random }) => number_random)
      .slice(0, 7);

    setNumberList(shuffledNumber);
  };

  // 번호가 뽑히는 것은 ? 이벤트 로그 안에 있어야 함

  // 우클릭하면 번호가 줄어듬 !

  // map - > 숫자 하나씩 뽑을 수 있다. 그리고 스타일을 적용하려면?
  //  숫자 마다 스타일을 걸어야 ...........

  // 이벤트 발생 버튼

  return (
    <div>
      <h2>
        <DollarCircleOutlined />
        로또 번호 출력
      </h2>

      <div onClick={handleClick}>
        <Button type="primary" icon={<SearchOutlined />}>
          Predict
        </Button>
      </div>
      {numList.map((num) => {
        return (
          <div key={num} style={{ ...style, backgroundColor: 'red' }}>
            {num}
          </div>
        );
      })}
    </div>
  );
}

// 예지 버튼 필요

// 컴포넌트의 고정된 스타일을 지정할 때 사용

const style = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  margin: '1rem',
  userSelect: 'none',
};

export default LottoPrecict;
