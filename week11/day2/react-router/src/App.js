import './App.css';
import {Link} from "react-router-dom"
function App() {
  return (
    <div className="App">
      <Link to ='/'>Home</Link>
      <Link to ='/about'>About</Link>
      <h1>React Router</h1>
    </div>
  );
}

export default App;
