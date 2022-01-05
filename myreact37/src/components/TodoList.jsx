import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Todo from './Todo';
import TodoForm from './TodoForm';
import './TodoList.css';

// 하나의 Todo만 가질 것이 아니라, 여러 개의 Todo를 해야 하니까
const INITIAL_STATE = [
  { content: '22년에는 꼭 취업하기' },
  { content: '파이썬 익히기' },
  { content: '리액트 익히기' },
];

function TodoList() {
  // onChange가 발생하면? inputText에 반영해야함
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  //custom hook
  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    // 초기값 지정하면 돼! 상황에 맞는 초깃값지정. 그냥 빈 오브젝트로 바꾸기만 할 게 아니라~
    content: '',
    color: 'Orange',
  });

  // 현재 fieldValues에 todo내역이 저장되어 있음
  const appendTodo = () => {
    console.log('새로운 TODO를 추가하겠습니다');
    const todo = { ...fieldValues }; // 오브젝트
    //  setter에 값 지정방식 : 배열
    // setTodoList([
    //   ...todoList, //기존의 todoList 추가
    //   todo,
    // ]);

    // setter에 함수 지정 방식
    setTodoList((prevTodoList) => [...prevTodoList, todo]);
    clearFieldValues();
  };

  // // 이 함수는 todoINdex를 받으면 해당 인덱스를 삭제 하겠다.
  // // 그럼 onclick으로 선택되면 ~
  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoIndex) =>
      prevTodoIndex.filter((_, index) => index !== todoIndex),
    ); // 인덱스만 가지고 true, false 리턴 -> 앞은 필요 없어서 언더바로 !
  }; // 다른 것만 삭제시킬 것이니까 index !== todoIndex
  return (
    <div className="todo-list">
      <h2>Todo List</h2>

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
        clear
      </button>

      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
        // <div onClick={() => removeTodo(index)}>{todo.content}</div>
      ))}
    </div>
  );
}

export default TodoList;
