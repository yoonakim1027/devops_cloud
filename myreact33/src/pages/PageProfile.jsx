import Axios from 'axios';

import { useState, useEffect } from 'react';
function PageProfile() {
  const [profileList, setProfileList] = useState([]); // 그냥..약속..
  useEffect(() => {
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
        setProfileList(axiosProfileList); // response.data<-  위에서 .get으로 받아온 데이터가 들어있음!
      })
      .catch((error) => {
        console.error(error);
      });
  }, []); // -> useEffect()는 마지막 인자로 [ ]를 받아줘야 함 .. 얘도.. 약속...
  // 비어있는 [] 가 언제 호출? 마운트되었을때. 초기 시작에 동작하려고 할때 이 함수가 자동호출이 되는것

  // 페이지 정보를 받기 위한 상탯값 정의
  const [userPage, setUserPage] = useState('bts-jin');
  return (
    <>
      <h2>PageProfile</h2>
      {/* 이 부분에 버튼으로 onClick -> 클리어 구성  */}
      {/* <button onClick(() => {}) >Clear</button>
      <button onClick={''}>Refresh</button> */}
      {/* 선택적 랜더링. && 앞에 있는 조건이 맞으면 뒤에 것을 렌더링(화면에 보여지는것) */}
      {/* .length -> 배열의 길이를 반환(배열은 순서가 있음) */}
      {profileList.length === 0 && <h4>"등록된 프로필이 없습니다." </h4>}

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
