import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faStickyNote } from '@fortawesome/free-solid-svg-icons';
import { faFacebook } from '@fortawesome/free-brands-svg-icons';
function ProfileCard({
  user,
  profileImage,
  name,
  role,
  github_url,
  email,
  changeUserPage,
}) {
  return (
    <>
      <h2>Profile Card</h2>

      <nav className="menu">
        <a href="#">
          <FontAwesomeIcon icon={faBars} />
        </a>
        <a href="#">
          <FontAwesomeIcon icon={faStickyNote} />
        </a>
      </nav>
      <article className="profile">
        <img src={profileImage} alt="프로필 이미지" />
        <h1>{name}</h1>
        <h2>{role}</h2>

        <a href="#" className="btnView">
          VIEW MORE
        </a>
      </article>

      <ul className="contact">
        <li>
          <FontAwesomeIcon icon={faFacebook} />
          <span> {github_url}</span>
        </li>
        <li>
          <FontAwesomeIcon icon={faStickyNote} />
          <span> {email}</span>
        </li>
      </ul>
      <nav className="others">
        <a onClick={() => changeUserPage('user0')}></a>
        <a onClick={() => changeUserPage('user1')}></a>
        <a onClick={() => changeUserPage('user2')}></a>
        <a onClick={() => changeUserPage('user3')}></a>
        <a onClick={() => changeUserPage('user4')}></a>
      </nav>
    </>
  );
}

export default ProfileCard;
