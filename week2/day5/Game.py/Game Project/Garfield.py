#minimum
# for loops
# clean code
# write article about what I dids  'dev.to'

# aim for mvp first

import re
from time import sleep
from unicodedata import name

def stars():
    print('*****************************************************')

class Character:
    def __init__(self,name,health,attack,items):
        self.name = name
        self.health = health
        self.attack = attack
        self.items = items

    def addItmes(self, items):
        self.items.append(items)
        print(f'Your current items are now..{self.items}')

    def printChar(self):
        # print(self.name,self.health,self.attack,self.items[0])
        print(f'Name: {self.name}, Health: {self.health}, Attack: {self.attack}, Items: {self.items}')
    
    def hitByAttack(self, damage):
        self.health -= damage 
        if self.health == 0:
            death()
            exit(0)

    def attackBigBoi(self, foe):
        foe.hitByAttack(self.attack)
        
def garfieldhit():
    print(f'Garfields new health is {megaCat.health}')

drawers = ['lighter']
garItems = ['gasoline']
def emptyItem(item):
    del item[0]



megaCat = Character('Garfield', 9000, 50, ['Lasagna'])
Jon = Character('Jon', 200, 10, ['cigarette'])

# Oddie = Character('Oddie', 200, 10, ['dog treat'])
# Valette = Character('Valette',150, 20, ['cat toy'])


def gameStart():
    print('\nYou are playing as "Jon" your stats are listed below:\n')
    Jon.printChar()
    stars()
    # sleep(7)
    print('Your once good buddy Garfield has turned into a monster.')
    # sleep(3)
    print("He is hiding somewhere in the house.....be careful.")
    # sleep(5)
    print('The lights in the house are continuing to flicker')
    print('Oddie has gone missing and you have been locked in your room for protection.')
    # sleep(5)
    print('You need to put an end to this nightmare, once and for all.') 
    # sleep(5)
    print( "You slowly unlock your door.\n")
    chooseRoom()
def chooseRoom():
    print(''' Where would you like to go?
        1. The Kitchen  
        2. The Garage 
        3. Outside the house
        4. Quit''')


    door = input("--> ")
    while door != '1' and door != '2' and door != '3' and door != '4':
        door = input("Please enter a number 1 - 4-->  ")
    if door == '1':
        kitchenEntry()
    if door == '2':
        garageOptions()
    if door == '3':
        outside()
    if door == '4':
        print('Garfield wickedly waves goodbye')
        

def kitchenEntry():
    stars()
    print('You cautiously make your way into the Kitchen.')
    # sleep(3)
    print('You notice an empty lasagna pan in the corner.')
    # sleep(3)
    print('You are overwhelmed by a foul stench.\n')
    # sleep(3)
    stars()
    kitchen()

def kitchen():
    sleep(1.5)
    print('''What do you want do:

        1. Grab the nearby gun
        2. Search the kitchen drawers
        3. Inspect the lasagna pan\n''')
    stars()
    kitChoice = input('--> ')
    while kitChoice != '1' and kitChoice != '2' and kitChoice != '3':
        kitChoice = input("Please enter a number 1 - 3 -->  ")
    if kitChoice == "1":
        print('You grab the gun and begin to inspect it. The lights go out.')
        # sleep(4)
        print('You look up and see a cat-like silhouette across the room!')
        # sleep(4)
        stars()
        print('''Do you?

        1. Shoot it!
        2. Fire a warning shot near the thing''')

        gun = input('--> ')
        while gun != '1' and gun != '2':
            gun = input("Please enter a number 1 or 2 -->  ")
        if gun == "1":
            print("The lights come back on, You point the gun and shoot Garfield")
            # sleep(2)
            print('''\n\n
The bullet demolishes one of Garfield's now 20 eyes. He suddenly appears as a 
15 foot monster with spider legs and a dark shroud fills the room.''')
            Jon.attackBigBoi(megaCat)
            garfieldhit()
            # sleep(7)
            print('''
Garfield is largely unaffected by the 
bullet and responds in perfect english:''')
            # sleep(4)
            print(' Bullets. Wont. Work.\n')
            stars()
            # sleep(3)  
            print('Garfield now lunges forward and attacks, causing damage and forcing the gun out of your hand')
            Jon.hitByAttack(megaCat.attack)
            print(f'Your health is now {Jon.health}')
            # sleep(3)
            print('You run to the garage')
            # sleep(3)
            stars()
            # sleep(4)
            garageOptions()
        elif gun == '2':
            print('You fire the warning shot.')
            print('The lights come back on, but continue to flicker.')
            print('Garfield stares at the new bullet hole in the hole, buying you time to escape.')
            print('You run into the garage and lock the door behind you, you hear garfield climb into the vents')
            stars() #or ask where to flee/travel
            garageOptions()
            #some sort of break/escape
        else:
            print('Please only type a number 1 - 2')
        
#KITCHEN 2nd OPTIon
    elif kitChoice == '2':
        if 'lighter' in drawers:
            print(f'You search the drawers and find a {drawers[0]}')
            Jon.addItmes(drawers[0])
            emptyItem(drawers)
            stars()
        else: print('You search the drawers but find nothing')
        
        kitchen()
#KITCHEN OPTION 3
    elif kitChoice == '3':
        print('You walk over and peer into the lasagna pan. The smell grows more intense.')
        print('You notice some strange remains at the bottom of the pan.')
        print('Every instinct you have is telling you to go back')
        # sleep(3)
        print('''What do you want to do?

        1. Go back
        2. Continue inspecting pan
        ''')
        
        gar3 = input('-->' )
        while gar3 != '1' and gar3 != '2':
            gar3 = input("Please enter a number 1 or 2 -->  ")   
        if gar3 == '1':
            kitchen()
        elif gar3 == '2':
            print("You feel a malevolant force push you into the pan.")
            # sleep(3)
            print("Garfield now seems to tower over the pan.")
            # sleep(3)
            print('He has a wide grin and says "You are the lasagna now, Jon."')
            # sleep(3)
            death()
#Preface
def preface():
    print(''' 
This game was inspired by the Youtube series: Garfield Gameboy'd and is a horror/adventure game featuring Garfield the cat. 
Are you smart enough to out wit a 46 year old cat? lets find out in this decision based text game


created by Ethan Gula with a very basic understanding of Python 3, copyright 2022
    ''')
    prefaceUser = input('Please enter "B" for back or "Q" to quit \n -->' )
    while prefaceUser != 'B' and prefaceUser != 'Q':
        prefaceUser = input('Please input B or Q \n --> ' )
    if prefaceUser == 'B':
            mainMenu()
    if prefaceUser == 'Q':
        print("Goodbye" )
        exit(0)
#MAIN MENU
def mainMenu():
    print('\n   Welcome to "GARFIELD: LARGER THAN LIFE" ')
    # sleep(3)
    print("""
            Main Menu\n\n
    1. Play
    2. Preface
    3. Exit
    """)
    choice = input("Indicate how you wish to proceed by typing in the number you've chosen \n --> ")
    while choice != '1' and choice != '2' and choice !='3':
        choice = input('Please choose a number 1- 3\n -->')
    if choice == '1':
            gameStart()
    elif choice == '2':
            preface()
    elif choice == '3':
            print('Goodbye' )
#DEATH
def death():
    print('Your hp has reached 0')
    print('Garfield unhinges his jaws and the world fades to black')
    # sleep(5)
    print('You lose...\n')
    playAgain = input('Want to play again? Y/N\n -->')
    while playAgain != 'Y' and playAgain != 'N':
        playAgain = input('Please type "Y" or "N"\n -->')
    if playAgain == 'Y':
        mainMenu()
    elif playAgain == 'N':
        print('Garfieled wickedly waves goodbye')
#GAROPTIONS
def garageOptions():
    print('You are now in the Garage')
    print('''What do you do?
        1. Walk over to the electrical box
        2. Fill a gasoline canister
        3. Inspect the weird bag in the corner
        4. Travel to a new room
    ''')
    garChoice = input('--> ')
    while garChoice != '1' and garChoice != '2' and garChoice != '3' and garChoice != '4':
        garChoice = input("Please enter a number 1 - 3 -->  ")
#GARAGE CHOICE ONE
    if garChoice == "1":
        print(''' 
        You walk over to the electrical box, but notice it doesnt want to open
        Do you:
        1. Go back
        2. Try to pry it open''')
        elect = input('-->')
        while elect != '1' and elect != '2':
            elect = input("Please enter a number 1 or 2 -->  ")
        if elect == '1':
            print ('You are now back in the center of the garage')
            garageOptions()
        elif elect == '2':
            print('''
While trying to force the box open you accidentally touch some live wires.''')
#garfield message and say youve opened box
        Jon.hitByAttack(50)
        print(f'Your new health is {Jon.health}')
        if Jon.health != 0:
            garageOptions()
#GARAGE CHOICE TWO
    elif garChoice == '2':
        if 'gasoline' in garItems:
            print(f'You pour {garItems[0]} into a canister and add it to your items')
            Jon.addItmes('gasoline')
            emptyItem(garItems)
            stars()
        else: print('There is no gasoline left')
        garageOptions()#or travel
#GARAGE  CHOICE THREE
    elif garChoice == '3':
        print('You walk over towards the bag')
        print
#GARAGE TRAVEL
    elif garChoice == '4':
        chooseRoom()
#OUTSIDE
def outside():
    print('You walk outside')
    print('''What do you want to do
    1. Run for it.
    2. End it all.
    3. Search the backyard
    4. Go back inside. 
    \n''')
    outChoice = input('-->')
    while outChoice != '1' and outChoice != '2' and outChoice != '3':
        outChoice = input('Please choose one of the above options only.')
    if outChoice == '1':
        print('''As you being to tkae your first steps something tells you this isnt right...
        This isn't how it ends.''')

    elif outChoice == '2':
        if 'cigarette' in Jon.items and '1' in Jon.items and 'gasoline' in Jon.items:
            endItAll()
        else:
            print('You do not have the required materials to end this nightmare.')
            print('You must go retrieve more items')
            chooseRoom()
    elif outChoice == '3':
        print
    elif outChoice == '4':
        chooseRoom()
#ENDITALL
def endItAll():
    print('You pour gasloine all over the parimeter of the house')
    # sleep(4)
    print('You use the lighter to light your cigarette')
    #sleep(4)
    print('After a few puffs you decide this is the only way')
    print('You toss the lit cigarette to ignit the gas that has now soaked into the house')
    print('You watch as your house burns to the ground. Its over.')
    sleep(8)
    print('''Ermerging from the flames are 40ft long bat wings, 
Garfield flys towards the heavens never to be seen again.
            ''')
    print('''A piece of burnt parchment falls in front of you. You can barely make out what it says:
    "What comes next is all for you Jon"''')


#GAME SEQUENCE

mainMenu()
