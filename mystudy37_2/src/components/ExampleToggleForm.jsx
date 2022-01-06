import { useState } from 'react';

function ExampleToggleForm() {
  const [showForm, setShowForm] = useState(false);
  // 삼항연산자를 참일때 위에, 거짓일 때 밑을 보여주기
  // 그런데 이렇게 되면 너무 길어져서, 거짓일때의 컴포넌트
  // 참의 컴포넌트를 따로 관리하는 것이 좋음!
  return (
    <div>
      <h2>ExampleToggleForm</h2>
      {!showForm && (
        <button
          onClick={() => setShowForm((prev) => !prev)}
          className="bg-yellow-300"
        >
          New Review
        </button>
      )}
      {showForm && <div className="bg-green-300">쓰기 폼</div>}
    </div>
  );
}
export default ExampleToggleForm;
