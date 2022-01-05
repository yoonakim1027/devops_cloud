function TodoForm({ fieldValues, handleChange, handleSubmit }) {
  // handleSubmit ->
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
      // 엔터키 호출 시, handleKeyPress 함수를 호출
    }
  };
  return (
    <div className="border-2 border-red-500 p-3">
      <h2 className="text-lg underline">TodoForm</h2>

      <input
        type="text"
        className="border-2 border-gray-200"
        onChange={handleChange}
        onKeyPress={handleKeyPress}
        name="content"
        value={fieldValues.content}
      />
      <button onClick={() => handleSubmit()}>저장</button>
      <select onChange={handleChange} name="color" value={fieldValues.color}>
        <option>Amber</option>
        <option>Orange</option>
        <option>Yellow</option>
      </select>
    </div>
  );
}

export default TodoForm;
