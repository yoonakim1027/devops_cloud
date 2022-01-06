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
  const [fieldValues, handleChange, clearFieldValues, setFieldValues] =
    useFieldValues({
      content: '',
      rating: 5,
    });

  // handlechange를 통해서 setFieldValues를 사용해야함(수정목적으로만 )
  const [viewForm, setViewForm] = useState(false);

  const changeBF = () => {
    setViewForm((viewForm) => !viewForm);
  };
  // 새로운 리뷰 저장 + 기존 리뷰 수정 -> id 유무로 구분
  const appendReview = () => {
    // 새로운 거 저장 : id X / 기존 것 저장 : id O
    let { id: reviewId } = fieldValues; // id가 있으면 가져올 것이고, 없으면 안가져올 것(undefined)

    // 새로운 리뷰 저장
    if (!reviewId) {
      reviewId = new Date().getTime();
      const createdreview = { ...fieldValues, id: reviewId }; //fieldValues에서 다 가져와서 리뷰를 구성
      setReviewList((prevReviewList) => [...prevReviewList, createdreview]);
    }
    // 기존 리뷰 수정 (map, filter 적절히 수정 )
    else {
      const editedReview = { ...fieldValues }; // 값을 새로 다시 받아옴!
      setReviewList((prevReviewList) =>
        prevReviewList.map((review) => {
          // 매 리뷰를 받음
          if (review.id === reviewId)
            //  매 루프를 도는 review.id 와, 수정된 대상인 reviewId가 같으면 ?
            return editedReview;
          return review;
        }),
      );
    }
    clearFieldValues();

    // review는 데이터베이스에 저장하면 id를 할당해준다
  };

  const deleteReview = (deletingReview) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter(
        ({ id: reviewId }) => reviewId !== deletingReview.id,
      ),
    ); // 배열안에 있는 항목들이 하나씩 넘어옴
  };

  // 새롭게 저장할 때에는 id가 없고
  // 수정할 때에는 id가 있음
  // id 유무를 통해 구분할 수 있음
  const willEditReview = (editingReview, id) => {
    console.log('willEditReview:', editingReview);
    setFieldValues(editingReview);
    setViewForm(true);
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
            handleEdit={() => willEditReview(review)}
            handleDelete={() => deleteReview(review)}
          />
        ))}
      </div>
    </div>
  );
}

export default ReviewList;
