import './App.css';
import PageTodoList from 'pages/PageTodoList';
import PageReviewList from 'pages/PageReviewList';
import { Routes, Route } from 'react-router-dom';
import TopNav from 'components/TopNav';
import PageNotFound from 'pages/PageNotFound';

function App() {
  return (
    <div className="app-center">
      <TopNav />
      <Routes>
        <Route path="/" element={<div>대문</div>} />
        <Route path="/reviews" element={<PageReviewList />} />
        <Route path="/todos" element={<PageTodoList />} />
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </div>
  );
}

export default App;
