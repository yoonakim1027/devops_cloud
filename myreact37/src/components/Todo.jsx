import './Todo.css';

function Todo({ todo, onClick }) {
  // todo와 onClick를 받겠다.

  return (
    <div
      className={`bg-${todo.color}-200 hover:${todo.color}-400 
      m-1 p-1 
      rounded-lg text-lg 
      border-blue-200 border-4 
      hover:border-blue-500 hover:scale-105 
      cursor-pointer`}
      onClick={onClick}
    >
      {todo.content}
      {todo.color}
    </div>
  );
}

export default Todo;
