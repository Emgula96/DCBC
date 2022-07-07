// what is a promise
//ana ction you take an you wait on an expected result 
//it will be what you wanted or not
//resolve or rejects
//async

//default optionare marked wtih *
//fetch
const functionName = async() => {
    const container = document.querySelector('#container');
    const pokemonCard = document.createElement("div");
    pokemonCard.classList = "pokemon-card"
    const pokemonName = document.createElement("h1")
    pokemonName.innerText = monster.name
    pokemonCard.appendChild(pokemonName)
    container.appendChild(pokemonCard)
//fetch form somwhere, this url
const url = "https://pokeapi.co/api/v2/pokemon/";
//await fetch
const response = await fetch(url);
const json = await response.json()
//convert to json
console.log(json.results)
for (const monster of json.results) {
    console.log(monster.name)
}
}
functionName();
