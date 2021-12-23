import { Input } from 'antd';
import { useState } from 'react';

function MelonSearch() {
  // 새로운 상탯값 정의
  const [query, setQuery] = useState(''); // 조회할때이름은 query, 변경하는 함수는 setQuery

  const handleChange = (e) => {
    const {
      target: { value },
    } = e;
    console.group('handleChange');
    console.log(value); // event 안에서 target 참조
    console.groupEnd();
    setQuery(value); // 쿼리라는 상탯값에서 검색어를 읽어오는 것
  };
  const handlePressEnter = () => {
    console.group('handlePressEnter');
    console.log(`검색어 ${query}로 검색합니다.`);
    console.groupEnd();
  };
  return (
    <div style={{ width: 300, margin: '0 auto' }}>
      <h2>멜론 검색</h2>
      검색어 : {query}
      <Input
        placeholder="검색어를 입력해주세요."
        onChange={handleChange} // 유저가 입력을 할때 호출되는 함수
        onPressEnter={handlePressEnter} // 유저가 엔터키를 눌렀을 때 호출되는 함수
        //Enter키를 눌렀을 때 호출되는 함수!
      />
    </div>
  );
}

export default MelonSearch;

// input의 i를 그냥 소문자로 하면? 리액트에서 지원하는 input 스타일
// Input으로 쓰면 위에서 스타일 적용한 대로 나옴
