import { useAppSelector, useAppDispatch } from "./app/hooks";
import './App.css';
import Homepage from "./components/Homepage";

function App() {
  // const counter = useAppSelector((state) => state.counter);
  const dispatch = useAppDispatch()
  return (
    <div className="App">
      <Homepage />
    </div>
  );
}

export default App;
