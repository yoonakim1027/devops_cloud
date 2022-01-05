// 자식 컴포넌트
import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Todo from './Todo';
import TodoForm from './TodoForm';

import './TodoList.css';

// 초기값 지정
const INITIAL_STATE = [
  { content: '22년 할 일', color: 'BlueViolet' },
  { content: '취업하기', color: 'Red' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    content: '',
    color: 'red',
  });

  // 클릭 시 나오는 index와 todoIndex가 같으면 == 클릭 시 삭제
  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  const appendTodo = () => {
    console.log('새로운 todo를 추가했습니다.');
    const todo = { ...fieldValues };

    // setter에 함수 지정
    setTodoList((prevTodoList) => [...prevTodoList, todo]);
    clearFieldValues();
  };
  return (
    <div className="todo-list">
      <h2>TodoList</h2>

      <TodoForm
        fieldValues={fieldValues}
        handleChange={handleChange}
        handleSubmit={appendTodo}
      />

      <hr />

      {JSON.stringify(fieldValues)}

      <button
        className="bg-red-500 text-gray-100 cursor-pointer"
        onClick={() => clearFieldValues()}
      >
        clear 버튼
      </button>

      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
      ))}
    </div>
  );
}

export default TodoList;
