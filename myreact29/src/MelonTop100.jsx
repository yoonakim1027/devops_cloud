// MelonTop100 컴포넌트 생성
/*
바뀌지 않는 데이터 -> 상탯값으로 지정하지 않아도 됨!
바뀌는 데이터만 상탯값으로 지정하면 됨 

{} -> object (배열 - array가 아님)
바뀌는 데이터는 전역변수를 안쓰는게 나음! 

- 값이 바뀌는 것은 상탯값으로 해야 변화가 저장된다! 

*/

import { useState } from 'react';

// 전역변수 : 바뀌지 않는 데이터
const initialSongList = [
  {
    'Unnamed: 0': 0,
    song_no: 32872978,
    title: 'Dynamite',
    album: 'Dynamite (DayTime Version)',
    artist: '방탄소년단',
    rank: 1,
    like: 354655,
  },
  {
    'Unnamed: 0': 1,
    song_no: 33077590,
    title: 'VVS (Feat. JUSTHIS) (Prod. GroovyRoom)',
    album: '쇼미더머니 9 Episode 1',
    artist: '미란이',
    rank: 2,
    like: 40716,
  },
  {
    'Unnamed: 0': 2,
    song_no: 32998018,
    title: '힘든 건 사랑이 아니다',
    album: '힘든 건 사랑이 아니다',
    artist: '임창정',
    rank: 3,
    like: 74236,
  },
];

// ul -> 순서가 없는 리스트를 만들때 사용
// ul>li*3 하고 엔터를 하면 li가 세줄이 자동생성
// const handleClick = () =>{};  -> arrow function
function MelonTop100() {
  const [SongList, setSongList] = useState([]); // songlist를 담을 것. -> 빈 [array]에서 시작
  const handleClick = () => {
    setSongList(initialSongList);
  };

  return (
    <div>
      <h2>멜론 top 100</h2>
      <button onClick={handleClick}>로딩</button>
      <ul>
        {SongList.map((song) => {
          // 한곡씩(song)나옴
          return <li>{song.title}</li>;
        })}
        <li>제목1</li>
        <li>제목2</li>
        <li>제목3</li>
      </ul>
    </div>
  );
}

export default MelonTop100;
