import PageLotto from 'pages/PageLotto';
import ProfileCard from 'components/ProfileCard';
import userList from 'components/data/profile.json';

// import profileImage1 from 'img/member4.jpg';
// import profileImage2 from 'img/member3.jpg';
// import profileImage3 from 'img/member2.jpg';
// import profileImage4 from 'img/member1.jpg';
import { useState } from 'react';

function App() {
  const [userNum, setuserNum] = useState('user1');
  return (
    <>
      {userList.map((user) => {
        if (userNum === user.user) {
          return (
            <ProfileCard
              name={user.name}
              role={user.role}
              github_url={user.github_url}
              email={user.email}
              changeUserPage={setuserNum}
            />
          );
        }
      })}

      <PageLotto />
    </>
  );
}

export default App;
