import React from 'react'

export default function Search(props) {
  return (
    <div>
      <input
        type="text"
        value={props.search}
        placeholder="search for a pokemon"
        onChange={(e) => {
        props.setSearch(e.target.value);
      }}
      />
    </div>
  );
}
