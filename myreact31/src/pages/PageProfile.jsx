import ProfileCard from 'components/ProfileCard';
import profileImage1 from 'img/member4.jpg';
import profileImage2 from 'img/member3.jpg';
import profileImage3 from 'img/member2.jpg';
import profileImage4 from 'img/member1.jpg';

function PageProfile() {
  return (
    <>
      <h2>Profile</h2>
      <ProfileCard
        name="김초롱"
        role="강아지"
        github_url="github.com/yoonakim1027"
        email="rlddbsk123@naver.com"
        image={profileImage1}
      />
      <ProfileCard
        name="김초랭"
        role="강쥐"
        github_url="github.com/yoonakim1027"
        email="rlddbsk123@naver.com"
        image={profileImage2}
      />
      <ProfileCard
        name="황꼬마"
        role="강아지"
        github_url="github.com/yoonakim1027"
        email="rlddbsk123@naver.com"
        image={profileImage4}
      />
      <ProfileCard
        name="김초롱"
        role="강아지"
        github_url="github.com/yoonakim1027"
        email="rlddbsk123@naver.com"
        image={profileImage3}
      />
    </>
  );
}

export default PageProfile;
