import PageLotto from 'pages/PageLotto';
import ProfileCard from 'components/ProfileCard';
import userList from 'components/data/profile.json';
import { useState } from 'react';

// index를 받으면 숫자를 받아옴
function App() {
  const [userNum, setUserNum] = useState('user0');
  return (
    <>
      {userList.map((user, index) => {
        if (userNum === user.user) {
          return (
            <div className={`user${index}`}>
              {/* 백틱을 사용한 방법2 */}
              <section>
                <ProfileCard
                  user={user.user}
                  name={user.name}
                  role={user.role}
                  github_url={user.github_url}
                  email={user.email}
                  profileImage={`/profile-images/member${index}.jpg`}
                  changeUserPage={setUserNum}
                />
              </section>
            </div>
          );
        }
      })}

      <PageLotto />
    </>
  );
}

export default App;
