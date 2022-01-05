// 새 커스텀 hook 생성
import { useState } from 'react';

function useFieldValues(initialFieldValues) {
  // 새로운 상탯값을 fieldValues 이름으로 조회
  const [fieldValues, setFieldValues] = useState(initialFieldValues);

  const clearFieldValues = () => setFieldValues(initialFieldValues);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFieldValues((prevFieldValues) => ({
      ...prevFieldValues,
      [name]: value,
    }));
  };
  return [fieldValues, handleChange, clearFieldValues];
}

export default useFieldValues;
