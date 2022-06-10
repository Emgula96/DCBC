listOfStuff = ['houst',  'car', 'backyard']
listOfCarStuff = ['headlights, Steeringwheel','clutch']
listOfClothes = ['shirt','pants','shoes', 'socks']

#functions are things we create to do steps we often repeat
#if you find yourself writing same code, make it a function
#functions allow us to do multiple steps over and 
#over but write code once

for stuff in listOfStuff:
    print(stuff+ " wow")


def printList(Listofthings):
    for stuff in Listofthings:
        print(stuff + " wow")

printList(listOfStuff)
printList(listOfCarStuff)
printList(listOfClothes)



def attack():
    print("I hit the monster")
while True:
    choice = ""
