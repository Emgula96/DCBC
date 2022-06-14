#to do list creat study garage neighbor enviornments
#introduce lits
#use a dictionary
#loop and nested loop?
#boolean?
#makebreakproof make user put what I want



# def breakProof():
#     if  != "1" or choice != "2" or choice != "3" or choice != " 4":
#         print("Please make a choice of 1,2,3, or 4 only")
#         return

from time import sleep


class Character:
    def __init__(self,name,health,attack,items):
        self.name = name
        self.health = health
        self.attack = attack
        self.items = items[0]

    def addItmes(self, items):
        self.item.append(items)

    def printChar(self):
        print(self.name,self.health,self.attack,self.items[0])

    def hitByAttack(self, damage):
        self.health =- damage     
        print(f'Your new health is {self.health}')

    def attackBigBoi(self, Garhp):
        Garhp =- self.attack
        print(f'Garfields new hp is{Garhp}')

megaCat = Character('Garfield', 9000, 50, ['Lasagna'])
Jon = Character('Jon', 200, 10, ['cigarette'])
Oddie = Character('Oddie', 200, 10, ['dog treat'])
Valette = Character('Valette',150, 20, ['cat toy'])



Jon.printChar()



def gameStart():
    
    print("You wake up in your house like any normal day. ")

    print(
    """
    Do you go to the 
    1. The Kitchen  
    2. The Study 
    3. The Garage
    4. The Neighbors
""")

    door = input("--> ")
    while door != '1' and door != '2' and door != '3' and door != '4':
        door = input("Please enter a number 1 - 4-->  ")
    if door == '1':
        kitchen()
    if door == '2':
        study()
    if door == '3':
        garage()
    if door == '4':
        neighbors()


def kitchen():

    print("You stumble upon Garfield.")
    print("You notice his lasagna pan is empty...")
    print('He is hungry....')
    sleep(2)
    print('Very.')
    sleep(2)
    print('Hungry.')
    sleep(2)
    print('You are overwhelmed by a foul stench')
    sleep(1.5)
    print ('''What do you do:

    1. Grab the nearset gun
    2. Fill his lasagna pan
    3. Inspect lasagna pan''')

    garfield = input('--> ')
    while garfield != '1' and garfield != '2' and garfield != '3':
        garfield = input("Please enter a number 1 - 3 -->  ")
    if garfield == "1":
        print('''Do you?

        1. Shoot Garfield
        2. Fire a warning shot in the air''')

        gun = input('--> ')
        while gun != '1' and gun != '2':
            gun = input("Please enter a number 1 or 2 -->  ")
        if gun == "1":
            print("You pick up the gun and shoot Garfield")
            sleep(2)
            print('''

The bullet demolishes one of Garfield's now 20 eyes. He suddenly appears as a 
25 foot monster with spider legs and a dark shroud fills the room.

*****************************************************

''')
            sleep(7)
            print('''
Garfield is largely unaffected by the 
bullet and responds in perfect english:''')
            sleep(4)
            print('''

Bullets...wont...work...Jon.

*****************************************************
            ''')
            sleep(3)  
            print('''
Garfield unhinges his jaws and everything fades to black...
''')
            sleep(3)
        elif gun == '2':
            print('You fire the warning shot.')
            print('Garfield stares at the passing bullet, buying you time to escape.')
            print('You run into the garage')
            garage()
            #some sort of break/escape

    elif garfield == '2':
        print('You fill Garfields pan')
        print('''
With malice in his voice, Garfield responds: 
"This does not satiate me, human I demand more"''')
        print('''What do you do?

        1. Beg for mercy
        2. Go to the store and buy more lasagna''')

        gar2 = input('-->' )
        if gar2 == '1':
            print('Garfield responds "I am your mercy"')
            print('Everything fades to black...')

        elif gar2 == "2":
            print('You manage to escape the house, and you set it on fire.')
            print('''
Ermerging from the flames are 40ft long bat wings, 
Garfield flys towards the heavens never to be seen again.
            ''')
            sleep(10)
            print('For now......')
            #printbreak/end

    elif garfield == '3':
        print('You walk over and fill the lasagna pan.')
        print('You notice some strange remains at the bottom of the pan.')
        sleep(3)
        print('''What do you want to do?

        1. Leave the room under the pretenses of getting more lasagna
        2. Continue inspecting pan.''')
        
        gar3 = input('-->' )
        if gar3 == '1':
            print('You leave the room and live the rest of your life in fear.')
        if gar3 == '2':
            print("You feel a malevolant force push you into the pan.")
            sleep(3)
            print("Garfield now seems to tower over the pan.")
            sleep(3)
            print('He has a wide grin and says "You are the lasagna now, Jon."')
            sleep(3)
            print("The world fades to black....")

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

def mainMenu():
    print('Welcome to "Garfield: Larger than life" ')
    print("""
    1. Play
    2. Preface
    3. Options
    4. Exit
    """)
    choice = input("Indicate option by typing in the number --> ")
    if choice == '1':
        gameStart()
    if choice == '2':
        preface()
    if choice == '3':
        options()
    if choice == '4':
        print('Goodbye' )
        Exit(0)

def garage():
    print('You stubmle into the garage and notice the lights are flickering... ')
    print('''What do you do?
    1.Walk over to the electrical box
    2.Walk over to the toolbox
    3.Inspect the weird bag in the corner
    ''')
    garChoice = input('--> ')
    while garChoice != '1' and garChoice != '2' and garChoice != '3':
        garChoice = input("Please enter a number 1 - 3 -->  ")
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
            garage()
        elif elect == '2':
            print('''
While trying to force the box open you accidentally touch some live wires and the world fades to black...''')
    elif garChoice == '2':
        print('')



#game sequence

mainMenu()