import Counter from 'components/Counter';

function PageCounter() {
  return (
    <>
      <h2>Counter</h2>
      <Counter initial={10} color={'blue'} />
      <Counter initial={10} color={'red'} />
      <Counter initial={10} color={'green'} />
    </>
  );
}

export default PageCounter;
// 꼭 function 이름을 잘 적어야 함
