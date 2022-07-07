

//grab elements that need from 

const dealerHand = document.getElementById('dealer-hand')
const playerHand = document.getElementById('player-hand')

const playGame = document.getElementById('deal-button')
const hitBtn = document.getElementById('hit-button')
const standBtn = document.getElementById('stand button') 

const suits = ['hearts','diamonds', 'spades', 'clubs']
const ranks = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

let deck = [];
let dealerCards = [];
let playerCards = [];




const makeDeck = (rank,suit) => {
const card = {
  rank: rank,
  suit: suit,
  pointValue: rank > 10 ? 10: rank,
}
deck.push(card);
}
const createCard = () => {
for(let suit of suits){
for (const rank of ranks){
  makeDeck(rank, suit);
}
};

const getCard = () =>{
const randomCard = Math.floor(Math.random()* deck.length -1) + 1;
const card = deck.splice(randomCard, 1)[0];
return card;
};

//getcardtest
// console.log(getCard())
// console.log(deck)


// const initialDeal = () =>{
// const pCard1 = getCard();
// const pCard2 = getCard();
// const dCard1 = getCard();
// const dCard2 = getCard();
// playerCards.push(pCard1,pCard2);
// dealerCards.push(dCard1, dCard2);
// renderCard(pCard1, playerHand);
// renderCard(pCard2, dealerHand);
// renderCard(dCard1, playerHand);
// renderCard(dCard2, dealerHand);
// }

const addPlayerCard = () => {
const card = getCard();
playerCards.push(card);
renderCard(card, playerHand);
};

const addDealerCard = () => {
const card = getCard();
dealerCards.push(card);
renderCard(card, dealerHand);
};


const renderCard = (card, targetElement) =>{
const img = document.createElement('img');
img.src = `./images/${card.rank}_of_${card.suit}.png`;
targetElement.append(img);
};

const dealCards = () => {
  addPlayerCard();
  addDealerCard();
  addPlayerCard();
  addDealerCard();
};


window.addEventListener('DOMContentLoaded', function() {
// Execute after page load
});

sdfjdkshf  

vccnbjvjdsfjskdlhfsdafweudcnbcjkfhdjfkhddskjlsdfkjhcnsdc
djfvnjndfjklnvjn
dfjdkhasfjlkasdf