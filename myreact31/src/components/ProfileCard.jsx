import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faStickyNote } from '@fortawesome/free-solid-svg-icons';
import { faFacebook } from '@fortawesome/free-brands-svg-icons';
import 'components/ProfileCard.css';
function ProfileCard({
  unique_id,
  name,
  role,
  mbti,
  instagram_url,
  profile_image_url,
  children,
}) {
  return (
    <>
      <h2>Profile Card</h2>0
      <nav className="menu">
        <a href="#">
          <FontAwesomeIcon icon={faBars} />
        </a>
        <a href="#">
          <FontAwesomeIcon icon={faStickyNote} />
        </a>
      </nav>
      <article className="profile">
        <img src={profile_image_url} alt="프로필 이미지" />
        <h1>{unique_id}</h1>
        <h1>{name}</h1>
        <h2>{role}</h2>
        <h2>{mbti}</h2>

        <a href="#" className="btnView">
          VIEW MORE
        </a>
      </article>
      <ul className="contact">
        <li>
          <FontAwesomeIcon icon={faFacebook} />
          <span> {instagram_url}</span>
        </li>
      </ul>
      <nav className="others">{children}</nav>
    </>
  );
}

export default ProfileCard;
