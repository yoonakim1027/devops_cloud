import PageProfile from 'pages/PageProfile';
import Axios from 'axios';

/*Stage 2. PageProfile에 profileList 상탯값을 정의하고, 
초기 상탯값으로 배열 안에 하나의 object만 선언하고, 
렌더 시에 profileList를 순회하여 매 속성을 텍스트/이미지로만 표현토록 합니다. 
텍스트는 h3/ul/li를 조합하여 표현합니다.
*/

function App() {
  return (
    <>
      <PageProfile>
        <div>
          <h2>PageProfile</h2>
        </div>
      </PageProfile>
    </>
  );
}

export default App;
