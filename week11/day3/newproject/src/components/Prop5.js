import React from 'react'

export default function Prop5(props) {
  return (
    <div>Prop5
      <h1>
        {props.houses.name}
      </h1>
      <h1>
        {props.houses.address}
      </h1>
    </div>
  )
}
