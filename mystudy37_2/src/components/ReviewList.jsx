import './ReviewList.css';
import { useState } from 'react';
import useFieldValues from 'hooks/useFieldValues';
import Review from './Review';
import ReviewForm from './ReviewForm';

const INITIAL_STATE = [
  { id: 1, content: '삼십 대의 내가 십 대, 이십 대의 나를 만났다', rating: 5 },
  {
    id: 2,
    content:
      ' 전 스파이더맨 두명이 자책했던 일들이 여기서 어느정도 구원받았다는거에 감사드립니다',
    rating: 5,
  },
  {
    id: 3,
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

  const [editForm, setEditForm] = useState(false);
  const [viewForm, setViewForm] = useState(false);

  const changeBF = () => {
    setViewForm((prevState) => !prevState);
  };
  // 새로운 리뷰 저장
  const appendReview = () => {
    // review는 데이터베이스에 저장하면 id를 할당해준다
    console.log('새로운 Review를 추가하겠습니다.');
    const reviewId = new Date().getTime();
    const review = { ...fieldValues, id: reviewId }; //fieldValues에서 다 가져와서 리뷰를 구성

    setReviewList((prevReviewList) => [...prevReviewList, review]);
    clearFieldValues();
  };

  const deleteReview = (deletingReview) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter(
        ({ id: reviewId }) => reviewId !== deletingReview.id,
      ),
    ); // 배열안에 있는 항목들이 하나씩 넘어옴
  };

  const editReview = (editingReview, id) => {
    setEditForm((prevReviewList) =>
      prevReviewList.filter((_, index) => index === editingReview),
    );
  };

  return (
    <div className="review-list">
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
      </div>
      <div>
        {!viewForm && (
          <button
            className="block justify-center w-full flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded cursor-pointer margin-5 top-5"
            type="button"
            onClick={() => changeBF()}
          >
            리뷰 작성
          </button>
        )}
        {viewForm && (
          <ReviewForm
            fieldValues={fieldValues}
            handleChange={handleChange}
            handleSubmit={appendReview}
            changeToButton={changeBF}
          />
        )}

        {reviewList.map((review, id) => (
          <Review
            key={review.id}
            review={review}
            handleEdit={() => editReview(review, id)}
            handleDelete={() => deleteReview(review)}
          />
        ))}
      </div>
    </div>
  );
}

export default ReviewList;
