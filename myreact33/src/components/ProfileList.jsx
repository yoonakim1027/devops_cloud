/*
> components/ProfileList 컴포넌트 (1개)
=> 다수 프로필에 대한 표현을 하며, 1개 프로필에 대한 표현은 ProfileCard 컴포넌트에 위임합니다.
=> 프로필 목록에 대한 레이아웃을 관리합니다.
=> 속성값으로 profileList 를 받고, 자식 컴포넌트인 ProfileCard 컴포넌트에는 속성값으로 profile 을 전달합니다.
=> components/ProfileList.css 를 만들고 연결합니다. 컴포넌트에는 className=""profile-list"" 를 기본으로 지정합니다."

*/
import ProfileCard from './ProfileCard';

function ProfileList({ dataProfile }) {
  return (
    <div>
      <h2>Profile List</h2>
      {dataProfile.length === 0 && <h4>등록된 프로필이 없습니다.</h4>}
      {dataProfile.map((profile) => {
        return <ProfileCard {...profile}></ProfileCard>;
      })}
    </div>
  );
}
export default ProfileList;
