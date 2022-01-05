import './ReviewList.css';
import { useState } from 'react';
import useFieldValues from 'hooks/useFieldValues';
import Review from './Review';
import ReviewForm from './ReviewForm';

const INITIAL_STATE = [
  { content: '삼십 대의 내가 십 대, 이십 대의 나를 만났다', rating: 5 },
  {
    content:
      ' 전 스파이더맨 두명이 자책했던 일들이 여기서 어느정도 구원받았다는거에 감사드립니다',
    rating: 5,
  },
  {
    content:
      '닥터옥토버스가 토비에게 "다컸구나 잘지냈니?" 는 어린시절 스파이더맨보고자란 사람들에게 하는말 같았고 토비의 "애쓰고있죠" 또한 내 상황에 너무 잘들어맞아 울컥했다',
    rating: 5,
  },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    content: '',
    rating: 5,
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
    <div className="md:flex md:items-center mb-6 text-center">
      <hr />
      <label
        className="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4"
        for="inline-full-name"
      >
        Review List
      </label>
      <br />
      <hr />
      <button
        className="text-center flex-shrink-0 bg-teal-500
         hover:bg-teal-700 border-teal-500 hover:border-teal-700 
         text-xl
         border-4
          text-white 
          py-3 px-40 
          rounded"
        type="button"
        onClick={() => {
          setViewForm(!viewForm);
        }}
      >
        {viewForm ? '메인으로 돌아가기' : 'New Review'}
      </button>
      {viewForm && (
        <ReviewForm
          fieldValues={fieldValues}
          handleChange={handleChange}
          handleSubmit={appendReview}
        />
      )}

      {reviewList.map((review, index) => (
        <Review review={review} onClick={() => removeReview(index)} />
      ))}
    </div>
  );
}

export default ReviewList;
