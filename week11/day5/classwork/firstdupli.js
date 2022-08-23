function firstDuplicate(arr) {
    let mySet = new Set()

for (let i = 0; i < arr.length; i++) { 
        if (mySet.has(arr[i])) {
            return arr[i]
        } else {
            mySet.add(arr[i]);
        }
    }
    return -1
}

const arr = [1, 1, 2, 3, 3, 2, 2];
console.log(firstDuplicate(arr));
