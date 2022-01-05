import './Todo.css';

function Todo({ todo, onClick }) {
  // todo와 onClick를 받겠다.

  return (
    <div
      className={`m-1 p-1 rounded-lg text-lg border-blue-200 border-2 hover:border-blue-500 hover:scale-105 cursor-pointer text-white`}
      style={{ backgroundColor: todo.color }}
      onClick={onClick}
    >
      {todo.content}
    </div>
  );
}

export default Todo;
