import PageAbout from 'pages/PageAbout';
import PageCounter from 'pages/PageCounter';
import TopNav from 'components/TopNav';
import { useState } from 'react';

function App() {
  const [pageName, setPageName] = useState('about');
  // 상탯값의 타입은 설정하기 나름! 가급적이면 타입을 유지시켜주는 것이 좋음 !

  // const changePageName = (pageName) => {
  //   setPageName(pageName);
  // };

  // 클릭하는 코드
  // 함수지만? 그냥 보면 일반 변수랑 같아보임
  // 함수나 클래스도 변수처럼 취급받을 수 있음
  // 함수도 속성값으로 내려줄 수 있음

  // const changePageName = () => {
  //   setPageName(pageName === 'counter' ? 'about' : 'counter');
  // };
  // 페이지 이름을 바꾸는 것

  return (
    <>
      <h1>김융구의 리액트</h1>

      <TopNav changePageName={setPageName} />
      {pageName === 'about' && <PageAbout />}
      {pageName === 'counter' && <PageCounter />}
    </>
  );
}

export default App;
// 선택적 렌더링 : 어떤 대상을 어떤 상황에 맞춰서 컴포넌트 자체를 렌더링 되게 할 수도있고~ 안되게 할수도 있고~
