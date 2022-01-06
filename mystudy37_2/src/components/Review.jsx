import './Review.css';
import Rating from './Rating';
import { useState } from 'react';

// review : 보여줄 review 객체

//handleEdit : 인자 없는 함수로 구 현, 수정 버튼 클릭 시에 호출
//handleDelete : 인자 없는 함수로 구현, 삭제 버튼 클릭 시에 호출

function Review({ review, onClick, handleDelete, handleEdit }) {
  const [showMenu, setShowMenu] = useState(false);

  // 인자가 없다는 설계대로 처리가 될 것
  const handleClickedEditButton = () => {
    if (handleEdit) {
      handleEdit();
    } else {
      console.warn('[Review] handleEdit 속성값이 지정되지 않았습니다.');
    }
  };

  // 실제 클릭을 하면? 이 버튼을 호출하도록 하는 것
  const handleClickedDeleteButton = () => {
    //handleDelete 값이 있다면? 호출, 없으면 아니도록
    if (handleDelete) {
      handleDelete(); // 참이라면 ? 호출
    } else {
      console.warn('[Review] handleDelete 속성값이 지정되지 않았습니다.'); // 경고
    }
  };

  return (
    <div
      onMouseEnter={() => setShowMenu(true)}
      onMouseLeave={() => setShowMenu(false)}
      className={` m-1 p-1 pt-5 rounded-lg text-lg border-green-500 border-2 hover:scale-105 relative`}
      style={{ backgroundColor: 'white' }}
      onClick={onClick}
    >
      {showMenu && (
        <div className="text-xs absolute top-0 right-0">
          <span
            onClick={handleClickedEditButton}
            className="text-green-700 hover:bg-green-300 cursor-pointer mr-1"
          >
            수정
          </span>
          <span
            onClick={handleClickedDeleteButton}
            className="text-red-700  hover:bg-red-300 cursor-pointer mr-1"
          >
            삭제
          </span>
        </div>
      )}

      {review.content}

      <Rating score={review.rating} />
    </div>
  );
}

export default Review;
