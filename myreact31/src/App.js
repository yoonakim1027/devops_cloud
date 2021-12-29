import PageLotto from 'pages/PageLotto';
import ProfileCard from 'components/ProfileCard';
//import userList from 'components/data/profile.json';
import { useState } from 'react';
import { Children } from 'react/cjs/react.production.min';
import Axios from 'axios';

const { useEffect } = require('react');

function App() {
  const [profileList, setProfileList] = useState([]);
  useEffect(() => {
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        setProfileList(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const [userNum, setUserNum] = useState('bts-jin'); // 페이지 넘어가기 위한 용도
  return (
    <>
      {profileList.map((user, index) => {
        if (userNum === user.unique_id) {
          return (
            <div key={user.unique_id} className={`user${index % 4}`}>
              <section>
                <ProfileCard
                  user={user.unique_id}
                  name={user.name}
                  role={user.role}
                  mbti={user.mbti}
                  instagram_url={user.instagram_url}
                  profile_image_url={user.profile_image_url}
                >
                  {profileList.map((user) => {
                    return (
                      <a
                        key={user.unique_id}
                        onClick={() => setUserNum(user.unique_id)}
                        className={user.unique_id === userNum ? 'on' : ''}
                      ></a>
                    );
                  })}
                </ProfileCard>
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
