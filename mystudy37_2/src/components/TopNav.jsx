import { Link } from 'react-router-dom';

function TopNav() {
  return (
    <div className="my-3">
      <ul className="flex gap-4">
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="/todos">Todos </NavLink>
        </li>
        <li>
          <NavLink to="/reviews">Reviews</NavLink>
        </li>
      </ul>
    </div>
  );
}
// Home, Todos, Reviews 는 children 속성인 셈 !
// 컴포넌트가 감싸고 있는 속성들은 컴포넌트로 넘겨야함
// 감싸고 있는 대상은 children
// 커스텀 NavLink
function NavLink({ to, children }) {
  return (
    <Link
      to={to}
      className="
      pb-1
      border-blue-400 
    hover:text-blue-400
    hover:border-b-4 duration-75
    text-m"
    >
      {children}
    </Link>
  );
}

export default TopNav;
