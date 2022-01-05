import { useState } from 'react';

// 함수
// 새로운 상탯값을 fieldValues 이름으로 조회,
// setFieldValues 이름으로 값 변경
function useFieldValues() {
  const [fieldValues, setFieldValues] = useState({});

  //이 함수는 setFieldValues만 관심있음
  const handleChange = (e) => {
    const { name, value } = e.target;

    // 함수 안 쓰고, 값 지정
    setFieldValues({
      ...fieldValues,
      [name]: value,
    });
  };

  // TODO
  return [fieldValues, handleChange];
}

export default useFieldValues;
