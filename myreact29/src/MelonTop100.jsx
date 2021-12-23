// MelonTop100 컴포넌트 생성
/*
바뀌지 않는 데이터 -> 상탯값으로 지정하지 않아도 됨!
바뀌는 데이터만 상탯값으로 지정하면 됨 

{} -> object (배열 - array가 아님)
바뀌는 데이터는 전역변수를 안쓰는게 나음! 

- 값이 바뀌는 것은 상탯값으로 해야 변화가 저장된다! 

*/

import { useState } from 'react';
import { Button as BootstrapButton } from 'react-bootstrap';
import { Button as AntdButton } from 'antd'; // import 이름을 바꾸려면? as 바꿀 이름 !
import Axios from 'axios'; // import 옆의 이름은 자기가 맘대로 조정가능
import initialSongList from 'data/melon_data.json';
import 'MelonTop100.css';

// 전역변수 : 바뀌지 않는 데이터

// ul -> 순서가 없는 리스트를 만들때 사용
// ul>li*3 하고 엔터를 하면 li가 세줄이 자동생성
// const handleClick = () =>{};  -> arrow function
function MelonTop100() {
  const [songList, setSongList] = useState([]); // songlist를 담을 것. -> 빈 [array]에서 시작
  const handleClick1 = () => {
    setSongList(initialSongList); // 현재 상수
  };
  const handleClick2 = () => {
    const url = 'https://antigravity-daejeon-2021.herokuapp.com/api/melon/';
    Axios.get(url) // 응답을 받아야함
      .then((response) => {
        const { data } = response;
        setSongList(data); // 서버로부터 받아오는 것
        // console.log('응답을 받았습니다.');
        // console.log(response);
      })
      .catch((error) => {
        console.error(error); // error는 .catch
      }); // 에러처리도 항상 수반되어야 한다
  };

  const handleClick3 = () => {
    setSongList([]); // setSongList에는 빈 array가 들어간다
  };

  return (
    <div>
      <h2>멜론 top 100</h2>
      <BootstrapButton variant="success" onClick={handleClick1}>
        파일 로딩
      </BootstrapButton>
      <AntdButton type="primary" onClick={handleClick2}>
        서버 로딩
      </AntdButton>

      <AntdButton type="dashed" onClick={handleClick3}>
        클리어
      </AntdButton>
      <ul className="songList">
        {songList.map((song) => {
          // 한곡씩(song)나옴
          return (
            <li key={song.song_no}>
              {song.rank} {song.title} by {song.artist}{' '}
            </li>
          );
        })}
        <li>제목1</li>
        <li>제목2</li>
        <li>제목3</li>
      </ul>
    </div>
  );
}
// 리액트는 map을 통해 반복되는 데이터가 있을 때
// 항상 제일 바깥에 있는 대상은? key라는 식별자 속성을 지정해줘야 한다.
// li에 추가!
// song_no -> 각각 노래들의 유일한 식별자!

export default MelonTop100;
