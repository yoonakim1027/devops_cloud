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

  // const changedInputText = (e) => {
  //   setInputText(e.target.value);
  //   // 값을 얻어오는 것
  //   //e는 이벤트 객체
  // };

  // const appendInputText = (e) => {
  //   console.log('e.key:', e.key);
  //   if (e.key === 'Enter') {
  //     console.log('inputText:', inputText);
  //     setTodoList((prevTodoList) => {
  //       return [...prevTodoList, { content: inputText }];
  //     }); // ... -> 원래 있던 배열 불러오기
  //     // 객체 {}
  //     // 위에서 {content : ''} 이런식으로 객체를 넣어줬기 때문에
  //     // 여기서도 {content: inputText} 이렇게 넣은 것

  //     setInputText('');

  //     //1. todoList 배열 끝에 inputText를 추가합니다
  //     // 2. inputText를 다시 비웁니다
  //     // => 현재는 input 박스 UI가 비어보이진 않을 거에요!
  //     // 수정이 아님! setTodoList에 함수를 넘기는 것! (이게 좋은 방식
  //     // todoList의 상탯값을 변경하는 것 X 배열의 push사용 X
  //   }
  // };

  // 현재 fieldValues에 todo내역이 저장되어 있음
  const appendTodo = () => {
    // setter에 값 지정방식
    console.log('새로운 TODO를 추가하겠습니다');
    const todo = { ...fieldValues }; // 오브젝트
    // 배열 !
    setTodoList([
      ...todoList, //기존의 todoList 추가
      todo,
    ]);
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

      {/* <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appendInputText}
      /> */}
      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
        // <div onClick={() => removeTodo(index)}>{todo.content}</div>
      ))}
    </div>
  );
}

export default TodoList;
