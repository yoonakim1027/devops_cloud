import './Review.css';
import Rating from './Rating';
import { useState } from 'react';
function Review({ review, onClick }) {
  const [showMenu, setShowMenu] = useState(false);
  return (
    <div
      onMouseEnter={() => setShowMenu(true)}
      onMouseLeave={() => setShowMenu(false)}
      className={`m-1 p-1 rounded-lg text-lg border-green-500 border-2 hover:scale-105 cursor-pointer `}
      style={{ backgroundColor: 'white' }}
      onClick={onClick}
    >
      {showMenu && (
        <div>
          <span>수정</span>
          <span>삭제</span>
        </div>
      )}

      {review.content}

      <Rating score={review.rating} />
    </div>
  );
}

export default Review;
