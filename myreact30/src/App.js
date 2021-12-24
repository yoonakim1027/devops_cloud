import PageAbout from 'pages/PageAbout';
import PageCounter from 'pages/PageCounter';
import TopNav from 'components/TopNav';
import { useState } from 'react';

function App() {
  const [pageName, setPageName] = useState('about');

  // 클릭하는 코드
  const handleClick = () => {
    setPageName(pageName === 'counter' ? 'about' : 'counter');
  };

  // 우클릭하면 번호가 줄어드는 코드
  const handleContextMenu = (e) => {
    // context menu의 기본 동작을 막는 코드
    e.preventDefault();
    setPageName(pageName - 1);
  };

  return (
    <>
      <h1>김융구의 리액트</h1>

      <button onClick={handleClick} onContextMenu={handleContextMenu}>
        페이지 토굴;
      </button>

      <TopNav />
      {pageName === 'about' && <PageAbout />}
      {pageName === 'counter' && <PageCounter />}
    </>
  );
}

export default App;
// 선택적 렌더링 : 어떤 대상을 어떤 상황에 맞춰서 컴포넌트 자체를 렌더링 되게 할 수도있고~ 안되게 할수도 있고~
