




const search = document.getElementById('SearchItem')

console.log("hey i work")
const searchDisc = async () =>{
    const url = `https://discitapi.herokuapp.com/disc`
    const userDisc = await fetch(url)
    const json = await userDisc.json()
    for (const discName of json) {
        const card = document.createElement('div')
        const thing = document.createElement('h1')
        card.id = 'card' 
        thing.innerText = discName.name
        card.append(thing)
        search.append(card)
        
    }
}


searchDisc()