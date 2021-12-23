import { Input } from 'antd';
import { useState } from 'react';
import Axios from 'axios';
import jsonpAdapter from 'axios-jsonp';

function MelonSearch() {
  // 새로운 상탯값 정의
  const [query, setQuery] = useState(''); // 조회할때이름은 query, 변경하는 함수는 setQuery
  const [songList, setSongList] = useState([]); // 새로운 상탯값을 정의하면서 그 상태값의 디폴트 값은 빈 array로 지정
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

    const url = 'https://www.melon.com/search/keyword/index.json';

    Axios({
      url: url,
      adapter: jsonpAdapter,
      callbackParamName: 'jscallback',
      params: {
        query: query,
      },
    })
      // .then이 결과값을 받음(오후 4시20분 경)
      .then((response) => {
        // 이름으로도 접근해서 데이터를 참조하고 싶다!
        // ALBUMCONTENTS, ARTISTCONTENTS
        const {
          data: { SONGCONTENTS: searchedSongList },
        } = response;
        // 응답에서 참조되는 값은 SONGCONTENTS이지만, (참조된 값은 변경할수 없고! )
        // 저장된 값은 searchedSongList라고 바꿔서 의미있게 저장할 수 있다.
        console.group('멜론 검색결과');
        console.log(response);
        console.log(searchedSongList);
        console.groupEnd();

        setSongList(searchedSongList); //값을 참조해서 이어서쓰는것
      })
      // error가 발생하면 .catch를 호출
      .catch((error) => {
        console.group('멜론 검색 에러');
        console.error(error);
        console.groupEnd();
      });
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
      {songList.map((song) => {
        return (
          <div>
            <img src={song.ALBUMIMG} />
            {song.SONGNAME} by {song.ARTISTNAME}
          </div>
        );
      })}
      {/* song 내역을 리액트 상에서 확인 가능 */}
    </div>
  );
}

export default MelonSearch;

// input의 i를 그냥 소문자로 하면? 리액트에서 지원하는 input 스타일
// Input으로 쓰면 위에서 스타일 적용한 대로 나옴
