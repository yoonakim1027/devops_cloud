import Axios from 'axios';

import { useState, useEffect } from 'react';

function PageProfile() {
  const [profileList, setProfileList] = useState([]); // useState는 초깃값으로 []빈 어레이를 초깃값으로 지정

  //Arrow function을 사용하기 위해선? const 변수명 () => {내용}

  // Stage 7. profile-list.json 조회에 실패했을 때,
  // "조회 시에 오류가 발생했습니다. 잠시 후 다시 시도해주세요." 라는 에러메세지를 띄워줍니다.
  // - 에러 여부를 기록하는 error 상탯값을 추가로 정의하고, 디폴트값은 null로 둡니다.
  //- 에러가 발생하면 에러객체를 저장하고, 통신이 시작될 때에는 에러 상탯값을 null로 초기화합니다.
  // - 본 동작을 테스트하기 위해, 조회 URL을 엉뚱하게 변경하고, 새로고침 버튼을 눌러 에러메세지 노출을 테스트합니다.
  const [error, setError] = useState(null);
  const handleRefresh = () => {
    setError(null); // 매 통신시 에러 초기화
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        const axiosProfileList = response.data.map((profile) => ({
          ...profile, // ... 하면 다 갖고온다 (unpacking)
          uniqueId: profile.unique_id,
          profileImageUrl: profile.profile_image_url,
          instagramUrl: profile.instagram_url,
        })); // 사용할 이름 : 데이터.데이터에 들어있는 key
        // () -> 변수를 여러개를 넘겨주는 거라서 소괄호는 리턴값을 보여주는 거고
        // {} -> 중괄호는 의미가 없는애고 원래 변수를 여러 개 넘겨주기 위해서는 중괄호를 써야한다
        setProfileList(axiosProfileList);
        // response.data<-  위에서 .get으로 받아온 데이터가 들어있음!
      })
      .catch((error) => {
        setError(error);
      });
    // 애초에 Axios 과정 자체를 리턴하게 되는 것
  };

  // 처음 실행 시, 새로 고침 시 바로 행해지는 함수
  // yarn start 해서 띄울때 바로 실행하기 위한 함수
  // 마운트는 한번...
  useEffect(() => {
    handleRefresh();
  }, []);
  // -> useEffect()는 마지막 인자로 [ ]를 받아줘야 함 .. 얘도.. 약속...
  // 비어있는 [] 가 언제 호출? 마운트되었을때. 초기 시작에 동작하려고 할때 이 함수가 자동호출이 되는것

  // 삭제 버튼
  const clearClick = () => {
    console.log(`clicked`);
    setProfileList([]);
  };

  return (
    <>
      <h2>PageProfile</h2>

      {/* 이 부분에 버튼으로 onClick -> 클리어 구성  */}
      <button onClick={clearClick}>Clear</button>
      <button onClick={handleRefresh}>Refresh</button>
      {/* 선택적 랜더링. && 앞에 있는 조건이 맞으면 뒤에 것을 렌더링(화면에 보여지는것) */}
      {/* .length -> 배열의 길이를 반환(배열은 순서가 있음) */}
      {profileList.length === 0 && <h4>등록된 프로필이 없습니다.</h4>}
      {error !== null && (
        <h3>조회 시에 오류가 발생했습니다. 잠시 후 다시 시도해주세요.</h3>
      )}
      {profileList.map((profile) => {
        return (
          <div key={profile.uniqueId}>
            <ul>
              <img src={profile.profileImageUrl} alt="프로필 이미지" />
              <li>{profile.uniqueId}</li>
              <h3>{profile.name}</h3>
              <li>{profile.role}</li>
              <li>{profile.mbti}</li>
              <li>{profile.instagramUrl}</li>
            </ul>
          </div>
        );
      })}
    </>
  );
}

export default PageProfile;
