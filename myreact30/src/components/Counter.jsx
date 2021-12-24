import { useState } from 'react';
// 임의의 속성값 color 추가 -> 문자열

function Counter({ initial, color }) {
  //속성값을 초기값으로 참조하여 상탯값 value를 생성
  const [value, setValue] = useState(initial); // 초기값(상탯값) 지정

  const handleClick = () => {
    setValue(value + 1); // 완벽한 코드는 아니지만, 어느정도 동작하는 코드
  };

  // 우클릭하면 번호가 줄어듬 !
  const handleContextMenu = (e) => {
    // context menu의 기본 동작을 막는 코드
    e.preventDefault();
    setValue(value - 1);
  };

  // style에 추가로 backgroundColor : color를 추가하려면 ?
  // ...style,
  //  backgroundColor
  return (
    <div
      style={{ ...style, backgroundColor: color }}
      onClick={handleClick}
      onContextMenu={handleContextMenu}
    >
      {value}
    </div>
  );
  // 함수의 인자는 대입된적이 없으면 undefiend
  // <상탯값 useState 설정 후 >
  // 여기서는 값을 initial로 참조할 게아니라, 위의 value 값을 받으면 됨!
  // 여기의 value는 위의 const에서 정의한 value

  //< 상탯값 useState설정 전 >>
  //부모인 Counter가 값을 넘겨줬으니까, 이는 속성값!
  // 각각의 컴포넌트가 있을 때?
  // 부모인 Counter로 부터 initial이라는 속성값(인자)를 받으면 ?
  // 이 인자에 기반해서 내가 이함수를 화면에 어떻게 보여주겠다는 것을 만들어서 리턴해주면
  // 이 리턴값이 화면에 보여지게 됨
}

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

export default Counter;

// ContextMenu

/* 
< 리액트에서 스타일 설정하는 방법 >

1. 외부에 스타일에 대한 오브젝트 선언
const style ~ 이렇게 선언 -> 변경은 안됨 
*/
