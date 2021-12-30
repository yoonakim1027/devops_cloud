/*"                > components/ProfileCard 컴포넌트 (반복)
 => 1개 프로필에 대한 표현을 하며, 개별 프로필에 대한 레이아웃을 관리합니다.
=> 속성값으로부터 profile 을 전달받아 표현합니다.
=> 속성값을 전달받아서 표현하는 것 외에 별도의 로직은 없습니다.
=> components/ProfileCard.css 를 만들고 연결합니다. 컴포넌트에는 className=""profile-card"" 를 기본으로 지정합니다." */
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faStickyNote } from '@fortawesome/free-solid-svg-icons';
import 'components/ProfileCard.css';

function ProfileCard({
  profileImageUrl,
  uniqueId,
  name,
  role,
  mbti,
  instagramUrl,
  children,
}) {
  return (
    <>
      <h2> Profile Card </h2>

      <section>
        <article className="profile-card">
          <img src={profileImageUrl} alt="프로필 이미지"></img>
          <h1>{uniqueId}</h1>
          <h2>{name}</h2>
          <h2>{role}</h2>
          <h2>{mbti}</h2>

          <article>
            <ul className="contact">
              <li>{instagramUrl}</li>
            </ul>
            <nav className="others">{children}</nav>
          </article>
        </article>
      </section>
    </>
  );
}

export default ProfileCard;
