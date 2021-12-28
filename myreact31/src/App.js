import PageLotto from 'pages/PageLotto';
import ProfileCard from 'components/ProfileCard';
import userList from 'components/data/profile.json';
import { useState } from 'react';
import { Children } from 'react/cjs/react.production.min';

// index를 받으면 숫자를 받아옴
// Stage 12. useState의 초기값을 하드코딩하지 마시고,
//  json 데이터를 참조하여, json 데이터 배열의 첫번째 값을 상탯값 초기값으로 활용해주세요.
// userList[0] - > 키를 참조할 때에는 "" 를 안쓰고 바로 참조가 가능하다.
function App() {
  const [userNum, setUserNum] = useState(userList[0].userID); // 원래는 여기서 그냥 user0 이름으로 받았는데,
  // 페이지 네임이 유저와 같을때 ? 어떤 데이터를 보여줄지가 밑의 코드
  return (
    <>
      {userList.map((user, index) => {
        if (userNum === user.userID) {
          return (
            <div className={`user${index}`}>
              {/* 백틱을 사용한 방법2 */}
              <section>
                <ProfileCard
                  user={user.userID}
                  name={user.name}
                  role={user.role}
                  github_url={user.github_url}
                  email={user.email}
                  profileImage={`/profile-images/member${index}.jpg`}
                >
                  {/* 이게 children이 되는 이유는? 부모 jsx안에 <nav>{children}</nav> 이라고 적용했기 때문에 !순서 대로 되는 것*/}
                  {userList.map((user) => {
                    return <a onClick={() => setUserNum(user.userID)}></a>;
                  })}
                  {/* 코드 정리 하기 ! ! 페이지 이름을 setUserNum으로 바꿔준다. 원래는 user1 이렇게 일일이 지정해줬었음  */}
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
