import './App.css';
import { useSelector, useDispatch } from 'react-redux'
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0"
/>;
function App() {
  const dispatch = useDispatch()
  const weather = useSelector(state => state.weather)
  const location = useSelector(state => state.location)
  
  const getWeather = async () => {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${APIKEY}&units=imperial`;
    const weatherJson = await fetch(url);
    const json = await weatherJson.json();
    dispatch({type:"SET_WEATHER", payload:json})
  };

  return (
    <div className="App">
      <div className="search">
        <input
          className="search-input"
          type="text"
          placeholder="Zipcode or City"
          onChange={(e) =>
            dispatch({
              type: "SET_LOCATION",
              payload: e.target.value,
            })
          }
        />
        <button
          className="search-btn"
          disabled={
            !location ? true : false
          }
          onClick={() => getWeather()}
        >
          SEARCH WEATHER
        </button>
      </div>
      <div className="container">
        <div className="top">
          <div className="City">
            <h1>{weather?.name}</h1>
          </div>
          <div className="feelsLike">
            <h2>
              {
                weather?.main
                  ?.feels_like
              }
            </h2>
          </div>
          <div className="wind">
            <marquee>
              <span class="material-symbols-outlined">
              </span>
              {weather?.wind?.speed}
            </marquee>
          </div>
          <div className="icon">
            <img
              className="icon-img"
              src={`http://openweathermap.org/img/wn/${weather?.weather?.[0].icon}@2x.png`}
              alt=""
            />
          </div>
        </div>

        <div className="bottom">
          <div className="humidity">
            <p className="bold">
              Humidity
            </p>
            <p>
              {weather?.main?.humidity}{" "}
              %
            </p>
          </div>

          <div className="high">
            <p className="bold">
              High of
            </p>
            <p>
              {weather?.main?.temp_max}
              °F
            </p>
          </div>

          <div className="low">
            <p className="bold">
              Low of
            </p>
            <p>
              {weather?.main?.temp_min}
              °F
            </p>
          </div>
        </div>
      </div>

      {/* <button onClick={()=>dispatch({type:"SAVE_CHANGEME", payload:"rocket"})}>Change Me</button> */}
      {/* <button onClick={() => dispatch({ type: "GET_USER" })}>GET USER</button> */}
    </div>
  );
}

export default App;
