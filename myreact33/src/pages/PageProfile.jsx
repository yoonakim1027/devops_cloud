import './PageProfile.css';
/*
> components/ProfileList 컴포넌트 (1개)
=> 다수 프로필에 대한 표현을 하며, 1개 프로필에 대한 표현은 ProfileCard 컴포넌트에 위임합니다.
=> 프로필 목록에 대한 레이아웃을 관리합니다.
=> 속성값으로 profileList 를 받고, 자식 컴포넌트인 ProfileCard 컴포넌트에는 속성값으로 profile 을 전달합니다.
=> components/ProfileList.css 를 만들고 연결합니다. 컴포넌트에는 className=""profile-list"" 를 기본으로 지정합니다."
전체 출력 페이지 -> 모든 상탯값을 여기서 정의해야 함

*/
import ProfileList from 'components/ProfileList';
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

    // e는 이벤트 내역을 알려주는 이벤트 객체
  };
  // 값이 있을때만 호출하고, 값이 없을때는 호출안함 -> 값이 없을때도 뭔가를 호출하도록 개선
  const handleKeyPress = (e) => {
    // e는 이벤트 내역을 알려주는 이벤트 객체
    // 여기서 값을 변경하면 안됨
    if (e.key === 'Enter') {
      const profileQuery = profileData.filter((member) => {
        return (
          member.name.toUpperCase().includes(query.toUpperCase()) ||
          member.role.toUpperCase().includes(query.toUpperCase()) ||
          member.mbti.toUpperCase().includes(query.toUpperCase())
        );
      }); // 여기서 리턴할 값을 profileQuery에 담았기 때문에,
      setProfileList(profileQuery); // 여기서 다시 페이지 정보를 넘기면 됨
    }

    // 포함되어 있는 값만 profile에 남게 됨
  };

  return (
    <div className="page-profile">
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

      {error !== null && (
        <h3>조회 시에 오류가 발생했습니다. 잠시 후 다시 시도해주세요.</h3>
      )}
      <ProfileList dataProfile={profileList} />
    </div>
  );
}

export default PageProfile;
