import './App.css';
import { useState } from 'react';
import students from './dummy';
import Header from './Header';
import Footer from './Footer';
import Left from './Left';
import Body from './Body';
import Right from './Right';

//multiple imports {students, tas}

//hook 
//change state in functional components

function App() {
  // this is the syntax to useState hook
  //const [stateVariable, function to change state var] = useState(default value for state)
  // const [students, setStudents] = useState([])
  //const [userData. setUserData] = useState({})
  //const [loading,setLoading] = useState(false)

  const [counter, setCounter] = useState(0)
  const [mood, setMood] = useState(false)
  return (
    <div className="App">
      <Header />
      
      <Left/>
      <Body/>
      <Right/>
      {/* <h1>Counter {counter}</h1>
      <button onClick={()=>setCounter(()=> counter +1)}>+</button>
      <button onClick={() => setCounter(() => counter - 1)}>-</button>
      
      
      <h1>How are you feeling today</h1>
      <h1>{mood ? "smiley tear" : "sad face"}</h1>
      <button onClick={() => setMood(!mood)}>Change mood</button> */}
      <Footer/>
    </div>
  );
}


export default App;
