import Counter from 'Counter';
// 여기서 부모는 Counter.jsx의 counter

function App() {
  return <Counter initial={10} />; // 속성으로 initial = 10
}
// 부모가 자식에게 key value를 넘김 -> 이를 속성값 이라고 함
// 인자에대한 이름이 initial => 인자에 대한 값이 {10}

//initial과 Counter의 initial의 이름은 같아야 한다

export default App;
