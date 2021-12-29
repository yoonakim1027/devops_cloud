/*Stage 2. PageProfile에 profileList 상탯값을 정의하고, 
초기 상탯값으로 배열 안에 하나의 object만 선언하고, 
렌더 시에 profileList를 순회하여 매 속성을 텍스트/이미지로만 표현토록 합니다. 
텍스트는 h3/ul/li를 조합하여 표현합니다.
*/
import { useState } from 'react';
function PageProfile() {
  const [profileList, setProfileList] = useState([
    {
      uniqueId: 'bts-jin',
      name: '진',
      role: '서브보컬',
      mbti: 'INFP',
      instagramUrl: 'https://instagram.com/jin',
      profileImageUrl:
        'https://classdevopscloud.blob.core.windows.net/data/bts-jin.jpg',
    },
  ]);

  return (
    <>
      <h2>PageProfile</h2>
      {/* 선택적 랜더링. && 앞에 있는 조건이 맞으면 뒤에 것을 렌더링(화면에 보여지는것) */}
      {profileList.length === 0 && <h4>"등록된 프로필이 없습니다." </h4>}

      {profileList.map((bts) => {
        return (
          <div key={bts.uniqueId}>
            <ul>
              <img src={bts.profileImageUrl} alt="프로필 이미지" />
              <li>{bts.uniqueId}</li>
              <h3>{bts.name}</h3>
              <li>{bts.role}</li>
              <li>{bts.mbti}</li>
              <li>{bts.instagramUrl}</li>
            </ul>
          </div>
        );
      })}
    </>
  );
}

export default PageProfile;
