import './Review.css';
import Rating from './Rating';
import { useState } from 'react';
function Review({ review, onClick }) {
  const [showMenu, setShowMenu] = useState(true);
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
          <span className="text-green-700 hover:bg-green-300 cursor-pointer mr-1">
            수정
          </span>
          <span className="text-red-700  hover:bg-red-300 cursor-pointer mr-1">
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
