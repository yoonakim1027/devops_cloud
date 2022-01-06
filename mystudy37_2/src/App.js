import './App.css';
import PageTodoList from 'pages/PageTodoList';
import PageReviewList from 'pages/PageReviewList';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<div>대문</div>} />
        <Route path="/reviews" element={<PageReviewList />} />
        <Route path="/todos" element={<PageTodoList />} />
      </Routes>
    </div>
  );
}

export default App;
