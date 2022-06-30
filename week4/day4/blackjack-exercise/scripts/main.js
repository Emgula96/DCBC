window.addEventListener('DOMContentLoaded', function() {
  // Execute after page load
})
const dealerHand = document.getElementById('dealer-hand')
const playerHand = document.getElementById('player-hand')
const deck = [];
const suits = ['hearts','diamonds', 'spades', 'clubs']
const ranks = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
const makeDeck = (rank,suit) => {

const card = {
  rank: rank,
  suit: suit,
  pointValue: rank > 10 ? 10: rank,
}
  deck.push(card);
}
  for(let suit of suits){
    for (const rank of ranks){
      makeDeck(rank, suit);
    }
  };
console.log(deck);

window.addEventListener("DOMContentLoaded", () => {});

const getCard = () =>{
const randomCard = Math.floor(Math.random()* deck.length -1) + 1;
return deck.splice(randomCard, 1);

}

//getcardtest
// console.log(getCard())
// console.log(deck)


const initialDeal = () =>{
  const pCard1 = console.log(getCard())
  const pCard2 = console.log(getCard())
  const dCard1 = console.log(getCard())
  const dCard2 = console.log(getCard())
  console.log(deck)
}
initialDeal()