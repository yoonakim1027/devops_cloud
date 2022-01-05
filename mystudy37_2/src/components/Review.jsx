import './Review.css';

function Review({ review, onClick }) {
  return (
    <div
      className={`m-5 p-5 text-lg border-green-200 border-4 hover:border-green-500 hover:scale-105 cursor-pointer text-black`}
      style={{ backgroundColor: 'white' }}
      onClick={onClick}
    >
      {review.content}
    </div>
  );
}

export default Review;
