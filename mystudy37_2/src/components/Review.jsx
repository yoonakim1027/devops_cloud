import './Review.css';
import Rating from './Rating';

function Review({ review, onClick }) {
  return (
    <div
      className={`m-1 p-1 rounded-lg text-lg border-green-500 border-2 hover:scale-105 cursor-pointer `}
      style={{ backgroundColor: 'white' }}
      onClick={onClick}
    >
      {review.content}

      <Rating score={review.rating} />
    </div>
  );
}

export default Review;
