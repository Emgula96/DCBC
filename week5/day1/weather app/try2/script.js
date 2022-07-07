const API_KEY = '78069d5042db8432db9959cf7e7079cb'
const timeEl = document.getElementById('time');
const dateEl = document.getElementById('date');
const currentWeatherItemsel = document.getElementsByClassName('weather-Item')
const timeZone = document.getElementById('time-zone')
const countryEl = document.getElementById('country')
const weatherForecastEl = document.getElementById('weatherforecast')

const search = document.getElementById('search')
const searchBar = document.getElementById('searchbar')
const currentWeather = document.getElementById('current-weather')
const humidity = document.getElementsByClassName('humid')
const feels = document.getElementsByClassName('fl')
const windSpeed = document.getElementsByClassName('Wind')
const currentTempEl = document.getElementsByClassName("cT");


const showTemp1 = (para) => {
showTemp.innerText = `${para}°F `;
currentTempEl.append(showTemp);
};

const showfl = (para) => {
  const feelslike = document.createElement("p");
  feelslike.innerText = `Feels Like: ${para}°F `;
  displayArea.append(feelslike);
};

const showWind = (para) => {
  const showwi = document.createElement("p");
  showwi.innerText = `Wind: ${para} mph`;
  displayArea.append(showwi);
};

const showHumidity = (para) => {
  const showhumid = document.createElement("p");
  showhumid.innerText = `${para}% humidty`;
  displayArea.append(showhumid);
};

const showCity = (para) => {
  const showci = document.createElement("h2");
  showci.innerText = `The Current Weather in ${para} is:`;
  displayArea.append(showci);
};

const searchWeather = async () => {
humidity.innertext = null
feels.innertext = null
windSpeed.innertext = null
currentTempEl.innertext = null
const searchBar = document.getElementById("searchbar").value;
const url = `https://api.openweathermap.org/data/2.5/weather?q=${searchBar},us&appid=${API_KEY}&units=imperial`;
console.log(searchBar);
const weatherData = await fetch(url);
const json = await weatherData.json();
console.log(json);
console.log(json.main.temp);
console.log(json.name);
showCity(json.name);
showTemp1(json.main.temp);
showHumidity(json.main.humidity);
showfl(json.main.feels_like);
showWind(json.wind.speed);
};
search.onclick = () => searchWeather();










const days = ['sunday','monday','tuesday','wednesday','thursday','friday']
const months = ['Jan','Fed','Mar','Apr','May','June','July','Aug','Sept','Nov',"Dec"]

setInterval(()=>{
    const time = new Date();
    const month = time.getMonth();
    const date = time.getDate();
    const day = time.getDay();
    const hour = time.getTime();
    const hoursIn12 = hour >= 13 ? hour %12: hour
    const minutes = time.getMinutes();
    const amPm = hour >= 12 ? "PM" : "AM"
    
    timeEl.innerhtml =
    hoursIn12 + ":" + minutes + "" + `<span id = "am-pm">${amPm}</span>`;

    dateEl.innerHTML = days[day] + ', ' + date + ' ' + months[month]
}, 1000)
// setInterval()

// const API_KEY = "78069d5042db8432db9959cf7e7079cb";
// const runBtn = document.getElementById("btn");
// const container = document.getElementById("container");
// const displayArea = document.getElementById("displayArea");


// const searchWeather = async () => {
//   displayArea.innerText = null;
//   const searchInput = document.getElementById("weatherBar").value;
//   const url = `https://api.openweathermap.org/data/2.5/weather?q=${searchInput},us&appid=${API_KEY}&units=imperial`;
//   console.log(searchInput);
//   const weatherData = await fetch(url);
//   const json = await weatherData.json();
//   console.log(json);
//   console.log(json.main.temp);
//   console.log(json.name);
//   showCity(json.name);
//   showTemp1(json.main.temp);
//   showHumidity(json.main.humidity);
//   showfl(json.main.feels_like);
//   showWind(json.wind.speed);
// };
// runBtn.onclick = () => searchWeather();



