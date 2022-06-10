#to do list creat study garage neighbor enviornments
#use more while loops
#introduce lits
#use a dictionary
#loop and nested loop?
#boolean?
#makebreakproof make user put what I want

# def breakProof():
#     while True:
#         breakProof = intput("--->")
#         try:
#             myAnswer = int(myAnswer)
#             return myAnswer
#         except:
#             print("Please choose a number from the options")


# def breakProof():
#     if  != "1" or choice != "2" or choice != "3" or choice != " 4":
#         print("Please make a choice of 1,2,3, or 4 only")
#         return

from sys import exit
from time import sleep

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

    if door == '1':
        kitchen()
    elif door == '2':
        study()
    elif door == '3':
        garage()
    elif door == '4':
        neighbors()

def kitchen():

    print("You stumble upon Garfield")
    print("you notice his lasagna pan is empty...")
    print('He is hungry....')
    sleep(2)
    print('Very.')
    sleep(2)
    print('Hungry.')
    print('You are overwhelmed by a foul stench')
    sleep(1.5)
    print ('''What do you do:

    1. Grab the nearset gun
    2. Fill his lasagna pan
    3. Inspect lasagna pan''')

    garfield = input('--> ')
    if garfield == "1":
        print('''Do you?

        1. Shoot garfield
        2. Fire a warning shot in the air''')

        gun = input('--> ')
        if gun == "1":
            print("You shoot at Garfield")
            sleep(2)
            print('''The bullet demolishes one of Garfield's 20 eyes he suddenly appears as a 25 foot monster with spider legs amd a dark shroud fills the room.''')
            sleep(7)
            print('''Garfield is largely uneffected by the bullet and responds in perfect english:''')
            sleep(2)
            print('Bullets...wont...work...Jon.')
            sleep(3)  
            print('''Garfield unhinges his jaws and everything fades to black...''')
            sleep(3)
        elif gun == '2':
            print('You fire the warning shot.')
            print('Garfield stares at the passing bullet, buying you time to escape.')
            #some sort of break/escape

    elif garfield == '2':
        print('You fill Garfields pan')
        print('He responds" This does not satiate me, human"')
        print('''What do you do?

        1. Beg for mercy
        2. Go to the store and buy more lasagna''')

        gar2 = input('-->')
        if gar2 == '1':
            print('Garfield responds "I am your mercy"')
            print('Everything fades to black...')

        elif gar2 == "2":
            print('You manage to escape the house, and you set it on fire.')
            print("Ermerging from the flames are 40ft long bat wings, Garfield flys towards the heavens never to be seen again.")
            sleep(10)
            print('For now......')
            #printbreak/end

    elif garfield == '3':
        print('You walk over to the lasagna pan')
        print('You notice some strange remains at the bottom of the pan')
        sleep(3)
        print('''What do you want to do?

        1. Leave the room under the pretenses of getting more lasagna.)
        2. Continue inspecting pan.''')
        
        gar3 = input('-->')
        if gar3 == '1':
            print('You leave the room and live the rest of your life in fear')
        if gar3 == '2':
            print("You feel a malevolant force push you into the pan")
            sleep(3)
            print("Garfield now seems to tower over the pan.")
            sleep(3)
            print('He has a wide grin and says "You are the lasagna now Jon."')
            sleep(3)
            print("The world fades to black....")


def mainMenu():
    print('Welcome to "Garfield: Larger than life"')
    print("""
    1. Play
    2. Preface
    3. Options
    4. Exit
    """)
    choice = input("Indicate option by typing in the number -->")
    if choice == '1':
        gameStart()
    if choice == '2':
        backgroundstory()
    if choice == '3':
        options()
    if choice == '4':
        print('Goodbye')
        Exit(0)

mainMenu()