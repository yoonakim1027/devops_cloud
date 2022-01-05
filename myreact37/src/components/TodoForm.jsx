import { useState } from 'react/cjs/react.development';

function TodoForm() {
  //하나의 상탯값으로 모든 필드의 값을 저장하고자 함
  const [fieldValues, setFieldValues] = useState({}); // 초기값은 빈 오브젝트 -> 그래야 키:밸류 형태

  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log('changed', name, value);

    // 함수 안쓰고 값을 지정
    setFieldValues({
      ...fieldValues,
      //추가로 변경할 값을 지정해야함.
      // 현재 name, value가 있음
      [name]: value, //계산된 속성인자
    }); // 값을 오브젝트로 지정해야 함
  };

  return (
    <div>
      <h2>TodoForm</h2>
      <input
        type="text"
        className="border-2 border-gray-400"
        onChange={handleChange}
        name="content"
      />
      <select onChange={handleChange} name="color">
        <option>Amber</option>
        <option>Orange</option>
        <option>Yellow</option>
      </select>

      <hr />
      {JSON.stringify(fieldValues)}
    </div>
  );
}

export default TodoForm;
