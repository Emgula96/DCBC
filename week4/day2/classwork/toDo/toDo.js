


const lsitContainer = document.getElementById('myList')
const addToDo = () =>{
    const inputField = document.getElementById("inputBox").value;
    console.log(inputField)
    const li = document.createElement("li")
    li.innerText = inputField
    lsitContainer.append(li)
}


add.onclick = addToDo();


