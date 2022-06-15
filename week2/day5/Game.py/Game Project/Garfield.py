#minimum
#1 class at a minimum
# functions
# for loops
# while loops
# list
# variables
# adding/removing aspects about your class
# the ability to exit the game
# the ability to replay the game
# clean code
# write article about what I dids  'dev.to'

# aim for mvp first

from time import sleep

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
        

    def attackBigBoi(self, foe):
        foe.hitByAttack(self.attack)
        
def garfieldhit():
    print(f'Garfields new health is {megaCat.health}')



megaCat = Character('Garfield', 9000, 50, ['Lasagna'])
Jon = Character('Jon', 200, 10, ['cigarette'])

# Oddie = Character('Oddie', 200, 10, ['dog treat'])
# Valette = Character('Valette',150, 20, ['cat toy'])


def gameStart():
    print('\nYou are playing as "Jon" your stats are listed below:\n')
    Jon.printChar()
    stars()
    sleep(7)
    print('Your once good buddy Garfield has turned into a monster.')
    sleep(3)
    print("He is hiding somewhere in the house.....be careful.")
    sleep(5)
    print('The lights in the house are continuing to flicker')
    print('Oddie has gone missing and you have been locked in your room for protection.')
    sleep(5)
    print('You need to put an end to this nightmare, once and for all.') 
    sleep(5)
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
        print('Garfieled wickedly waves goodbye')
        

def kitchenEntry():
    stars()
    print('You cautiously make your way into the Kitchen.')
    sleep(3)
    print('You notice an empty lasagna pan in the corner.')
    sleep(3)
    print('You are overwhelmed by a foul stench.\n')
    sleep(3)
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
        print('You grab the gun and begin to inspect it')
        sleep(4)
        print('You look up and see that Garfield has appeared in front of you!')
        sleep(4)
        stars()
        print('''Do you?

        1. Shoot Garfield
        2. Fire a warning shot near garfield''')

        gun = input('--> ')
        while gun != '1' and gun != '2':
            gun = input("Please enter a number 1 or 2 -->  ")
        if gun == "1":
            print("You point the gun and shoot Garfield")
            sleep(2)
            print('''\n\n
The bullet demolishes one of Garfield's now 20 eyes. He suddenly appears as a 
25 foot monster with spider legs and a dark shroud fills the room.''')
            Jon.attackBigBoi(megaCat)
            garfieldhit()
            sleep(7)
            print('''
Garfield is largely unaffected by the 
bullet and responds in perfect english:''')
            sleep(4)
            print(' Bullets. Wont. Work.\n')

            stars()
            sleep(3)  
            print('Garfield now lunges forward and attacks, causing damage and forcing the gun out of your hand')
            Jon.hitByAttack(megaCat.attack)
            print(f'Your health is now {Jon.health}')
            sleep(3)
            print('You run to the garag')
            garageOptions()
        elif gun == '2':
            print('You fire the warning shot.')
            print('Garfield stares at the passing bullet, buying you time to escape.')
            print('You run into the garage')
            garageOptions()
            #some sort of break/escape
        else:
            print('Please only type a number 1 - 2')
        
#KITCHEN 2nd OPTIon
    elif kitChoice == '2':
        #fix item counter here ==0 print drawers are empty
        drawers = ['Lighter']
        print(f'You search the drawers and find a {drawers}')
        Jon.addItmes('Lighter')
        kitchen()
#KITCHEN OPTION 3
    elif kitChoice == '3':
        print('You walk over and peer into the lasagna pan. The smell grows more intense.')
        print('You notice some strange remains at the bottom of the pan.')
        sleep(3)
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
            sleep(3)
            print("Garfield now seems to tower over the pan.")
            sleep(3)
            print('He has a wide grin and says "You are the lasagna now, Jon."')
            sleep(3)
            death()
            
def preface():
    print(''' 
This game was inspired by the Youtube series: Garfield Gameboy'd and is a horror/adventure game featuring Garfield the cat. 
Are you smart enough to out wit a 46 year old cat? lets find out in this decision based text game


created by Ethan Gula with a very basic understanding of Python 3, copyright 2022
    ''')
    prefaceUser = input('Please enter "B" for back or "Q" to quit -->' )
    while prefaceUser != 'B' and prefaceUser != 'Q':
        prefaceUser = input('Please input B or Q--> ' )
        if prefaceUser == 'B':
            mainMenu()
        if prefaceUser == 'Q':
            print("Goodbye" )
            break
#MAIN MENU
def mainMenu():
    print('\n   Welcome to "GARFIELD: LARGER THAN LIFE" ')
    sleep(3)
    print("""
            Main Menu\n\n
    1. Play
    2. Preface
    3. Exit
    """)
    choice = input("Indicate how you wish to proceed by typing in the number you've chosen \n --> ")
    while choice != '1' and choice != '2' and choice !='3':
        choice = input('Please choose a number 1- 3\n')
    if choice == '1':
            gameStart()
    elif choice == '2':
            preface()
    elif choice == '3':
            print('Goodbye' )

def death():
    print('Garfield unhinges his jaws and the world fades to black')
    sleep(5)
    print('You lose...\n')
    palyAgain = input('Want to play again? Y/N\n -->')
    while palyAgain != 'Y' and palyAgain != 'N':
        input('Please type "Y" or "N"\n -->')
    if palyAgain == 'Y':
        mainMenu()
    elif palyAgain == 'N':
        print('Garfieled wickedly waves goodbye')



def garageOptions():
    print('You are now in the Garage')
    print('''What do you do?
        1. Walk over to the electrical box
        2. Fill a gasoline canister
        3. Inspect the weird bag in the corner
    ''')
    garChoice = input('--> ')
    while garChoice != '1' and garChoice != '2' and garChoice != '3':
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
        garageOptions()
#GARAGE CHOICE TWO
    elif garChoice == '2':
        print('')
#GARAGE  CHOICE THREE

def outside():
    print('You walk outside')
    print('''What do you want to do
    1. Run for it
    2. End it all.
    3. Go back inside 
    \n''')
    outChoice = input('-->')
    while outChoice != '1' and outChoice != '2' and outChoice != '3':
        outChoice = input('Please choose one of the above options only.')
    if outChoice == '1':
        print('''As you being to tkae your first steps something tells you this isnt right...
        This isn't how it ends.''')

    elif outChoice == '2':
        #condition statements to check inventory
        if Jon.items != ['cigarette','lighter','gasoline']:
            print('You do not have the required materials to end this nightmare.')
            print('You must go inside and retreive')
            chooseRoom()
    elif outChoice == '3':
        chooseRoom()




#game sequence

mainMenu()