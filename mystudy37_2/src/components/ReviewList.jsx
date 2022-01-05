import './ReviewList.css';
import { useState } from 'react';
import useFieldValues from 'hooks/useFieldValues';
import Review from './Review';
import ReviewForm from './ReviewForm';

const INITIAL_STATE = [
  { content: '삼십 대의 내가 십 대, 이십 대의 나를 만났다' },
  {
    content:
      ' 전 스파이더맨 두명이 자책했던 일들이 여기서 어느정도 구원받았다는거에 감사드립니다',
  },
  {
    content:
      '닥터옥토버스가 토비에게 "다컸구나 잘지냈니?" 는 어린시절 스파이더맨보고자란 사람들에게 하는말 같았고 토비의 "애쓰고있죠" 또한 내 상황에 너무 잘들어맞아 울컥했다',
  },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    review: '',
  });

  const [viewForm, setViewForm] = useState(false);

  // 해당하는 리뷰 -> 클릭 시 삭제
  const removeReview = (reviewIndex) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter((_, index) => index !== reviewIndex),
    );
  };

  // 리뷰 append
  const appendReview = () => {
    console.log('새로운 Review를 추가하겠습니다.');
    const review = { ...fieldValues };

    setReviewList((prevReviewList) => [...prevReviewList, review]);
    clearFieldValues();
  };

  return (
    <div className="review-list">
      <hr />
      <h2>ReviewList</h2>

      <hr />
      <button
        className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
        type="button"
        onClick={() => {
          setViewForm(!viewForm);
        }}
      >
        {viewForm ? '' : ''}
        New Review
      </button>
      {viewForm && (
        <ReviewForm
          fieldValues={fieldValues}
          handleChange={handleChange}
          handleSubmit={appendReview}
        />
      )}

      <button
        className="flex-shrink-0 border-transparent border-4 text-teal-500 hover:text-teal-800 text-sm py-1 px-2 rounded cursor-pointer"
        type="button"
        onClick={() => clearFieldValues()}
      >
        삭제!
      </button>

      {reviewList.map((review, index) => (
        <Review review={review} onClick={() => removeReview(index)} />
      ))}
    </div>
  );
}

export default ReviewList;
