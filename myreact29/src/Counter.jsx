import { useState } from "react"; // 리액트에서는 이런식으로 import
// 상탯값은 어떠한 타입도 가능하다~
// useState(초기값)-> 참조할 수 있도록 어떤 값을 받아야함!
// useState는 항상 값을 두개 -> 배열로 받음!
// [이름은 고정된 것이 아니고~ ]
// [상탯값(일반적인 변수와는 다르게, 값을 참조하는 이름),값을 변경하는 이름 ]
// -> 이름이 다르다!
// 상탯값은 읽어오는 이름, 변경하는 이름임 다르다!

// handleClick시마다 색이 변경되게 하려면 ?

function Counter() {
  const [value, setValue] = useState(0); // Counter밑에 바로 써야함! 순서가 중요하다
  const [color, setColor] = useState("red");
  // 밖의 중괄호는 값을 저장하는 공간일뿐이다~
  const handleClick = () => {
    console.log(`clicked`);
    setValue(value + 1);
    setColor(value % 2 === 0 ? "green" : "red"); // 삼항연산자 사용
    // value를 2로 나눈 나머지가 0이라면? 참이면 green / 거짓이면 red
  };
  return (
    <div
      style={{
        backgroundColor: color,
        width: 100,
        height: 100,
        display: "inline-block",
        margin: 5,
        borderRadius: 50,
        textAlign: "center",
        userSelect: "none",
        cursor: "pointer", // 커서가 올라갈때 커서가 변경
      }}
      onClick={handleClick}
    >
      <span>{value}</span>
    </div>
  );
}
//위의 value임 !
// 첫번째 카운터 클릭 시에만 첫번째 카운터의 값만 올라갔으면 좋겠다
// 각각의 컨퍼런스가 각가의 설정을 유지해야 함
// 이 설정을? 상탯값(state)라고 함
// 각각의 컨포넌트가 따로 갖고 있는 값을 상탯값이라고 함

export default Counter;
// export default Counter -> 카운터 컴포넌트를 하나 만든 것
// 카운터만 임포트해서 바로 적용하는 것
