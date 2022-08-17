import React, { useState } from "react";
import "../App.css";

export default function PokeCard(props) {
  const [front, setFront] = useState(true);
  return (
      <div className="container">
      <div className="card">
        <h2>{props?.pokemon?.name}</h2>
              <h3>{props?.pokemon?.hp}</h3>
              <button onClick={() => {props.deleteCard(props.pokemon) }}>delete</button>
        <img
          onClick={() => setFront(!front)}
          src={
            front
              ? props?.pokemon?.sprites?.front
              : props?.pokemon?.sprites?.back
          }
          alt=""
        />
      </div>
    </div>
  );
};

