import React from 'react'
import { useState } from 'react'


export default function Body() {
    const [input, setInput] = useState('');
    const [todo, setTodo] = useState([]);
    const [todoItem,setToDoItem] = useState("")

    const addToDo = () => {
        setTodo(...todo, todoItem);
        setToDoItem("");
    };

    const deleteToDo = (item) => {
        const filteredTodoList = todo.filter((todo) => todo !== item)
        // setToDo(filteredTodoList);
    }

    return (
        <div className='body'>
            {/* <form className="todo-form">
            <input
                type="text"
                placeholder="Add a todo"
                value={input}
                name = 'text'
                className='todo-inpout' />
            <button className='add-todo'>Add To List</button>
        </form> */}
            <h1>Add a to do item</h1>
            <input value={todoItem} onChange={(e) => setToDoItem(e.target.value)} type="text" />
            <button onClick={() => addToDo()}>Submit</button>
            {todo.map((todo, i) => (
                <>
                <p>{todo}</p>
                    <button onClick={() => deleteToDo(todo)}>X</button>
                </>
            ))}
        </div>
    );
}