const blue = [6,9,2,4,5]
const red = [5,8,1,3,4]
newRed = red.sort()
newBlue = blue.sort()

const heighCheck = () =>{
    arr = []
    for (let i = 0; i < newBlue.length; i++) {
    arr.append(newBlue[i] > newRed[i])
}
}

heighCheck()