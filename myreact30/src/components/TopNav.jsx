import './TopNav.css';
function TopNav({ changePageName }) {
  return (
    <ul className="top-nav">
      <li>
        <a onClick={() => changePageName('about')}>About</a>
      </li>
      <li>
        <a onClick={() => changePageName('counter')}>카운터</a>
      </li>
      <li>
        <a onClick={() => changePageName('lotto')}>로또</a>
      </li>
      <li>
        <a onClick={() => changePageName('playlist')}>플레이리스트</a>
      </li>
    </ul>
  );
}

// TopNav !
// 관련된 스타일링은 이 컴포넌트 내에서 하는 것
// 이것도 App.js 에서 가져와야 함!
export default TopNav; //이름을 그대로 써줘야 함!

// 상탯값을 부모가 가지고 있고? 변경하는 것은 자식이 할 수도 있음
// 자식이 TopNav -> 부모가 App.js
