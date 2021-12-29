import Axios from 'axios';

import { useState, useEffect } from 'react';

function PageProfile() {
  const [profileData, setProfileData] = useState([]); // 전체 데이터 받을 상탯값
  const [profileList, setProfileList] = useState([]); // search 시 변화 필드를 받을 상탯값
  const [query, setQuery] = useState(null); // query 입력 값 받을 상탯값
  const [error, setError] = useState(null); // error 발생 시 객체를 받을 상탯값

  const handleRefresh = () => {
    setError(null); // 매 통신시 에러 초기화
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        const axiosProfileList = response.data.map((profile) => ({
          ...profile,
          uniqueId: profile.unique_id,
          profileImageUrl: profile.profile_image_url,
          instagramUrl: profile.instagram_url,
        }));
        setProfileData(axiosProfileList);
      })
      .catch((error) => {
        setError(error);
      });
  };
  // 재시동 !
  useEffect(() => {
    profileData.length === 0 && handleRefresh();
    setProfileList(profileData);
  }, [profileData]); // 전체 데이터인 profileData를 dependent

  const handleChange = (e) => {
    const value = e.target.value;
    setQuery(value);
    // e는 이벤트 감지. e가 target -> click를 감지
  };

  // profile : JSON 파일의 모든 데이터
  // Object.values(profile) : profile의 (키)값만 받아옴
  // .some : some() 메서드는 배열 안의 어떤 요소라도 주어진 판별 함수를 통과하는지 테스트,
  //        => True, False로 반환. 빈 배열일 경우에도 False 반환
  //        .some((search) => search에 들어갈 값은, 위에서 profile의 값만 받아온 데이터
  // .include : includes() -> 배열이 특정 요소를 포함하고 있는지 판별
  // 결국, search.includes(query)  -> query의 값이 search(profile의 모든 value 값)에 포함되어있는지 판별

  const handleKeyPress = (e) => {
    // e는 이벤트 감지
    if (e.key === 'Enter') {
      if (
        query &&
        setProfileList(
          // query가 포함된 값만 남는걸로 상탯값 변경
          profileData.filter((profile) =>
            Object.values(profile).some((info) => info.includes(query)),
          ), // 포함되어 있는 값만 profile에 남게 됨
        )
      );
    }
  };
  return (
    <>
      <h2>PageProfile</h2>
      <>
        <input
          type="text"
          placeholder="검색어를 입력해주세요."
          onChange={handleChange}
          onKeyPress={handleKeyPress}
        />
      </>

      <button onClick={() => setProfileList([])}>Clear</button>
      <button onClick={handleRefresh}>Refresh</button>

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
