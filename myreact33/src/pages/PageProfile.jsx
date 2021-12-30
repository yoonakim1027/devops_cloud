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
    // 변화를 감지 하라고 ......
    const value = e.target.value;
    setQuery(value);

    // e는 이벤트 감지. e가 target -> click를 감지
  };
  // 값이 있을때만 호출하고, 값이 없을때는 호출안함 -> 값이 없을때도 뭔가를 호출하도록 개선
  const handleKeyPress = (e) => {
    // e는 이벤트 내역을 알려주는 이벤트 객체
    // 여기서 값을 변경하면 안됨
    if (e.key === 'Enter') {
      const profileQuery = profileData.filter((member) => {
        return (
          // filter는
          member.name.includes(query) ||
          member.role.includes(query) ||
          member.mbti.includes(query)
        );
      });
      setProfileList(profileQuery);
    }

    // 포함되어 있는 값만 profile에 남게 됨
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
