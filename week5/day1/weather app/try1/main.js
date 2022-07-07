const API_KEY = '78069d5042db8432db9959cf7e7079cb'
const runBtn = document.getElementById("btn")
const container = document.getElementById('container')
const displayArea = document.getElementById('displayArea')



const showTemp1 = (para) =>{
const showTemp = document.createElement('h2')
showTemp.innerText = `${para}°F `;
displayArea.append(showTemp)
}

const showfl = (para) =>{
const feelslike = document.createElement('p')
feelslike.innerText = `Feels Like: ${para}°F `;
displayArea.append(feelslike)
}


const showWind = (para) =>{
const showwi = document.createElement('p')
showwi.innerText = `Wind: ${para} mph`
displayArea.append(showwi)
}

const showHumidity = (para) =>{
const showhumid = document.createElement('p')
showhumid.innerText = `${para}% humidty`
displayArea.append(showhumid)
}

const showCity = (para) =>{
    const showci = document.createElement('h2')
    showci.innerText = `The Current Weather in ${para} is:`
    displayArea.append(showci)
}




const searchWeather = async () =>{
    displayArea.innerText = null
    const searchInput = document.getElementById("weatherBar").value
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${searchInput},us&appid=${API_KEY}&units=imperial`;
    console.log(searchInput)
    const weatherData = await fetch(url);
    const json = await weatherData.json()
    console.log(json);
    console.log(json.main.temp);
    console.log(json.name);
    showCity(json.name)
    showTemp1(json.main.temp);
    showHumidity(json.main.humidity);
    showfl(json.main.feels_like)
    showWind(json.wind.speed)

};
runBtn.onclick = () => searchWeather();