import "./App.css";
import Prop1 from "./components/Prop1";
import {
  useEffect,
  useState,
} from "react";
import PokeCard from "./components/PokeCard";
import Search from "./components/Search";

function App() {
  const state = {
    pokemon: [
      {
        pokemon: [
          {
            id: 1,
            name: "bulbasaur",
            hp: 45,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png",
            },
          },
          {
            id: 2,
            name: "ivysaur",
            hp: 60,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/2.png",
            },
          },
          {
            id: 3,
            name: "venusaur",
            hp: 80,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/3.png",
            },
          },
          {
            id: 4,
            name: "charmander",
            hp: 39,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/4.png",
            },
          },
          {
            id: 5,
            name: "charmeleon",
            hp: 58,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/5.png",
            },
          },
          {
            id: 6,
            name: "charizard",
            hp: 78,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/6.png",
            },
          },
          {
            id: 7,
            name: "squirtle",
            hp: 44,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/7.png",
            },
          },
          {
            id: 8,
            name: "wartortle",
            hp: 59,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/8.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/8.png",
            },
          },
          {
            id: 9,
            name: "blastoise",
            hp: 79,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/9.png",
            },
          },
          {
            id: 10,
            name: "caterpie",
            hp: 45,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/10.png",
            },
          },
          {
            id: 11,
            name: "metapod",
            hp: 50,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/11.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/11.png",
            },
          },
          {
            id: 12,
            name: "butterfree",
            hp: 60,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/12.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/12.png",
            },
          },
          {
            id: 13,
            name: "weedle",
            hp: 40,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/13.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/13.png",
            },
          },
          {
            id: 14,
            name: "kakuna",
            hp: 45,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/14.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/14.png",
            },
          },
          {
            id: 15,
            name: "beedrill",
            hp: 65,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/15.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/15.png",
            },
          },
          {
            id: 16,
            name: "pidgey",
            hp: 40,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/16.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/16.png",
            },
          },
          {
            id: 17,
            name: "pidgeotto",
            hp: 63,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/17.png",
            },
          },
          {
            id: 18,
            name: "pidgeot",
            hp: 83,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/18.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/18.png",
            },
          },
          {
            id: 19,
            name: "rattata",
            hp: 30,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/19.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/19.png",
            },
          },
          {
            id: 20,
            name: "raticate",
            hp: 55,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/20.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/20.png",
            },
          },
        ],
      },
    ],
  };
  const [counter, setCounter] =
    useState(0);
  const [pokemon, setPokemon] =
    useState(state.pokemon[0].pokemon);

  const [search, setSearch] = useState("");

  const deleteCard = (item) => {
    const filteredCards = pokemon.filter((pokemon) => pokemon !== item);
    setPokemon(filteredCards);
  }



  // useEffect(() => {
  //   console.log("counter is set in useeffect");
  //   setCounter(counter + 1);
  // }, []);

  // 1
  // this will run one time for sure, and will always run if the dom is updated
  // useEffect(() => {
  //   const fetchPokemon = async () => {
  //     const response = await fetch("https://pokeapi.co/api/v2/pokemon");
  //     const json = await response.json();
  //     setPokemon(json.results);
  //     console.log(json);
  //   };
  //   fetchPokemon();
  // }, [counter]);

  // 2
  // this will run one time for sure, and will run if the state variable is updated or the dom is updated
  // useEffect(() => {
  //   console.log("useffect running");
  //   // setCounter(counter + 1);
  // }, [counter]);

  // 3 runs one time and then one more time when the dom updates and thats it
  // useEffect(() => {
  //   console.log("useeffect is running")
  //   setCounter(counter + 1)
  // });

  // const houses = [
  //   {
  //     title: "Joes Beach House",
  //     address: "123 Main St USA",
  //   },
  //   {
  //     title: "Joes Beach House 2",
  //     address: "1232 Main St USA",
  //   },
  // ];
  // const owner = {
  //   firstName: "Joe",
  //   lastName: "Frasier",
  // };

  // const data = ["joe", "tim", "josh"];
  return (
    <div className="App">
      <Search
        search={search}
        setSearch={setSearch} /> 
      {pokemon?.filter((pokemon) => pokemon.name.includes(search)).map(
        (pokemon) => {
          return (
            <PokeCard
              key={pokemon.name}
              pokemon={pokemon}
              deleteCard = {deleteCard}
            />
          );
        },
      )}
      {/* <Prop1 houses={houses} owner={owner} /> */}
    </div>
  );
}

export default App;