import { useState } from 'react';

// 함수
// 새로운 상탯값을 fieldValues 이름으로 조회,
// setFieldValues 이름으로 값 변경
// 인자로 초기값을 받으면? 이것들이
// useState에도 초깃값으로 들어가고
// setFieldValues의 {}에도 값이 들어감
function useFieldValues(initialFieldValues) {
  const [fieldValues, setFieldValues] = useState(initialFieldValues);
  // 빈 오브젝트로 클리어
  const clearFieldvalues = () => setFieldValues(initialFieldValues);
  //이 함수는 setFieldValues만 관심있음
  const handleChange = (e) => {
    const { name, value } = e.target;

    // // 함수 안 쓰고, 값 지정
    // setFieldValues({
    //   ...fieldValues,
    //   [name]: value,
    // });
    setFieldValues((prevFieldValues) => ({
      ...prevFieldValues,
      [name]: value,
    }));
  };

  // TODO
  return [fieldValues, handleChange, clearFieldvalues];
}

export default useFieldValues;
