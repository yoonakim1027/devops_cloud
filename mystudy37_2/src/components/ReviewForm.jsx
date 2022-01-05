function ReviewForm({ fieldValues, handleChange, handleSubmit }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <>
      <div className="flex items-center text-center border-b border-red-500 py-2">
        <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
          <svg
            class="fill-current h-4 w-4"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
          </svg>
        </div>

        <div className="w-full md:w-1/2 px-10 mb-6 md:mb-0">
          <label
            className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-5"
            for="grid-first-name"
          >
            ♥ 리뷰 작성 ♥
          </label>
          <label
            className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-5"
            for="grid-first-name"
          >
            별점
            <select
              className="text-center block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
              onChange={handleChange}
              name="rating"
              value={fieldValues.rating}
            >
              <option>5</option>
              <option>4</option>
              <option>3</option>
              <option>2</option>
              <option>1</option>
            </select>
          </label>
          <br />
          <textarea
            cols="47"
            rows="5"
            type="text"
            className="appearance-none block w-full h-full bg-gray-200 text-gray-700 border border-green-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
            id="grid-first-name"
            onChange={handleChange}
            onKeyPress={handleKeyPress}
            name="content"
            value={fieldValues.content}
          />
          <h4 className="text-red-500 text-xs italic ">리뷰를 작성해주세요.</h4>
          <div>
            <button
              className="text-center flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded cursor-pointer margin-5 top-5"
              type="button"
              onClick={() => handleSubmit()}
            >
              저장하기
            </button>
          </div>
        </div>
      </div>
    </>
  );
}

export default ReviewForm;
