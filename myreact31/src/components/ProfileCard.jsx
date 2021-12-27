import { useState } from 'react/cjs/react.development';
import profileImage from 'img/member1.jpg';

function ProfileCard({ name, role, github_url, email, changeUserPage }) {
  return (
    <div>
      <h2>Profile Card</h2>
      <section>
        <nav className="menu">
          <a href="#">
            <i className="fas fa-bars"></i>
          </a>
          <a href="#">
            <i className="fas fa-sticky-note"></i>
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
            <i className="fas fa-envelope"></i>
            <span>{github_url}</span>
          </li>
          <li>
            <i className="fas fa-envelope"></i>
            <span>{email}</span>
          </li>
        </ul>
        <nav className="others">
          <a onClick={() => changeUserPage('user1')}></a>
          <a onClick={() => changeUserPage('user2')}></a>
          <a onClick={() => changeUserPage('user3')}></a>
          <a onClick={() => changeUserPage('user4')}></a>
        </nav>
      </section>
    </div>
  );
}

export default ProfileCard;
