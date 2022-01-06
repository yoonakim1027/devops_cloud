import './App.css';
import PageTodoList from 'components/pages/PageTodoList';
import PageReviewList from 'pages/PageReviewList';
import { Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <div>
      <Routes>
        <Route to="/" element={<div>대문</div>} />
        <Route to="/reviews" element={<PageReviewList />} />
        <Route to="/todos" element={<PageTodoList />} />
      </Routes>
    </div>
  );
}

export default App;
