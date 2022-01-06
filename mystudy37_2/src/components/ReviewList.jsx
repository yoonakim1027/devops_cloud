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
  // 이거는 그냥 실행 되면 알아서 prevState를 읽음
  // 받을 인자가 없어서 -> 그냥 호출이되면? 바로 실행
  // 저장하기 버튼을 누르면 바로 화면전환을 원하는 거라서
  // 함수는 ? 인자가 없으면 호출되자마자 실행
  // 인자가 있으면 그 인자를 꼭 !! 받아야 실행
  const changeBF = () => {
    setViewForm((prevState) => !prevState);
  }; // 얘는 인자가 없어서 바로 실행. 실행되는 것 자체는?

  // // 이거는 prevState이라는 인자가 있어야 실행됨
  // const changeBFex = (prevState) => {
  //   setViewForm(!prevState);
  // };
  // 현재 ReviewForm에서는 prevState라는 상탯값이 없기 때문에 인자로 받지 못함.

  // 리뷰 append
  const appendReview = () => {
    console.log('새로운 Review를 추가하겠습니다.');
    const review = { ...fieldValues };

    setReviewList((prevReviewList) => [...prevReviewList, review]);
    clearFieldValues();
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
            className="block justify-center w-full"
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

        {reviewList.map((review, index) => (
          <Review review={review} />
        ))}
      </div>
    </div>
  );
}

export default ReviewList;
