import Counter from 'Counter';
//import { Fragment } from 'react'; // 예전엔 이렇게 썼는데~
// 이제는 그냥 안쓰고 <> </> 이렇게 태그 안에를 비워도 된다 ~

// 여기서 부모는 Counter.jsx의 counter

function App() {
  return (
    <>
      <Counter initial={10} color={'blue'} />
      <Counter initial={10} color={'red'} />
      <Counter initial={10} color={'green'} />
    </>
  );
  // div로 안감싸고 여러개를 하면 오류남!
  // 한 묶음으로 해줘야 ㅎ오류가 안난다 .
  //리액트의 제약 사항 : 한개를 반환해야 한다 .

  // 그냥 태그명안쓰고 <> </> 라고 하면? div 없이도 가능
  // Fragment -> 실제로 그려지는 것은 아니고, 논리적으로 한 묶음이라는 것을 표현하는 것

  // 속성으로 initial = 10
}
// 부모가 자식에게 key value를 넘김 -> 이를 속성값 이라고 함
// 인자에대한 이름이 initial => 인자에 대한 값이 {10}

//initial과 Counter의 initial의 이름은 같아야 한다

export default App;
