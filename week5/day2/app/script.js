const random = document.getElementById('random')
const container = document.getElementById('container')
const displayArea = document.getElementById('displayArea')
const picture = document.getElementById('picture')
const nameDrink = document.getElementById('name-drink')
const ingred = document.getElementById('ingredients')
const instruc = document.getElementById('instructions')
const ratio = document.getElementById('ratio')
const glass = document.getElementById('glass')
const ititle = document.getElementById('ititle')

const showDrinkName = (para)=>{
    const showEle = document.createElement('p')
    showEle.innerHTML = `Drink Name: <span>${para}</span>`;
    nameDrink.append(showEle)
}
const showDrinkGlass = (para)=>{
    const showEle = document.createElement('p')
    showEle.innerHTML = `Glass Needed: <span>${para}</span>`
    glass.append(showEle)
}
const showDrinkIngred = (para)=>{
    const showEle = document.createElement('li')
    showEle.innerHTML = `${para}`
    if (para != null){
        ingred.append(showEle)}
}
const showDrinkPicture = (para)=>{
    picture.style.backgroundImage = `url('${para}')`
}
const addTitle = () =>{
    const newTitle = document.createElement('h3')
    newTitle.innerText = 'Ingredients'
    ititle.append(newTitle)
    
}



const searchCocktail = async () =>{
    nameDrink.innerText = null
    ingred.innerText = null
    glass.innerText = null
    ititle.innerText = null
    const url = `https://www.thecocktaildb.com/api/json/v1/1/random.php`;
    const randomCocktail = await fetch(url);
    const json = await randomCocktail.json()
    console.log(json.drinks[0])
    addTitle()
    showDrinkName(json.drinks[0].strDrink)
    showDrinkGlass(json.drinks[0].strGlass)
    showDrinkIngred(json.drinks[0].strIngredient1)
    showDrinkIngred(json.drinks[0].strIngredient2)
    showDrinkIngred(json.drinks[0].strIngredient3)
    showDrinkIngred(json.drinks[0].strIngredient4)
    showDrinkIngred(json.drinks[0].strIngredient5)
    showDrinkPicture(json.drinks[0].strDrinkThumb)
}


random.onclick = () => searchCocktail()