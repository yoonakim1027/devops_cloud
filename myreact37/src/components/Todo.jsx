import './Todo.css';

function Todo({ todo, onClick }) {
  // todo와 onClick를 받겠다.

  return (
    <div className="bg-blue-300" onClick={onClick}>
      {todo.content}
    </div>
  );
}

export default Todo;
