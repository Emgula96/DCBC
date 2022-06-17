from time import sleep
def stars():
    print('**********************************************************')
# class Character:
#     def __init__(self,name,health,attack,items):
#         self.name = name
#         self.health = health
#         self.attack = attack
#         self.items = items

#     def addItmes(self, items):
#         self.items.append(items)
#         print(f'Your current items are now..{self.items}')

#     def printChar(self):
#         print(f'Name: {self.name}, Health: {self.health}, Attack: {self.attack}, Items: {self.items}')
    
#     def hitByAttack(self, damage):
#         self.health -= damage 
#         if self.health == 0:
#             death()
#             exit(0)

#     def attackBigBoi(self, foe):
#         foe.hitByAttack(self.attack)
        
# def garfieldhit():
#     print(f'Garfields new health is {megaCat.health}')

# drawers = ['lighter']
# garItems = ['gasoline']
# def emptyItem(item):
#     del item[0]

# megaCat = Character('Garfield', 9000, 50, ['Lasagna'])
# Jon = Character('Jon', 200, 10, ['cigarette'])




def endAlltxt():
    print('You pour gasoline all over the perimeter of the house')
    sleep(4)
    print('You use the lighter to light your cigarette.')
    sleep(4)
    print('After a few puffs you decide this is the only way.')
    sleep(3)
    print('You toss the lit cigarette to ignite the gas that has now soaked into the house.\n')
    sleep(3)
    stars()
    print('You watch as your house burns to the ground. It\'s over.\n')
    sleep(8)
    print('''Ermerging from the flames are 40ft long bat wings, 
Garfield flies towards the heavens never to be seen again.
            ''')
    sleep(3)
    stars()
    print('''A piece of burnt parchment falls in front of you. You can barely make out what it says:
    "What comes next is all for you. Jon."''')
    stars()
    sleep(3)
    stars() 
    sleep(3)
    stars()
    sleep(3)
    stars()
    sleep(3)
    stars()
    print('You survived! Thank you for playing!!')


def prefaceLog():
    print(''' 
    This game was inspired by the Youtube video: Garfield Gameboy'd and is a horror/adventure game featuring Garfield the cat. 
    Are you smart enough to out wit a 46 year old cat? lets find out in this decision based text game


    created by Ethan Gula with a very basic understanding of Python 3, copyright 2022
        ''')
    stars()


# vent = 'open'
# def study():
#     print('You have arrived in the Study.')
#     print('''What would you like to do?

#     1. Inspect your desk
#     2. Close the open vent above the desk
#     3. Walk over to the bookshelf 
#     4. Tavel to a different room
#     ''')
#     stars()
#     studyInput = input('-->')
#     while studyInput != '1' and studyInput != '2' and studyInput != '3' and studyInput != '4':
#         studyInput = input('Please only enter a number 1 - 4')

# #GOING TO DESK issues with vent
#     if studyInput == '1'and vent == 'open':
#         print('You walk over and sit down at your desk')
#         print('Oh no you forgot to shut the vent!!!')
#         print('Garfield claws you from inside the vent.')
#         sleep(3)
#         Jon.hitByAttack(megaCat.attack)
#         print(f'Your new health is {Jon.health}.')
#         print('You shut the vent preventing further onslaught.')
#         vent = 'closed'
#     elif studyInput == '1' and vent == 'closed':
#         print('''Do you
#         1. Try to unlock your desk
#         2. Go back ''')
#         desk = input ('-->')
#         while desk != '1' and desk != '2':
#             desk = input('Only enter a 1 or 2')
#         print('You sit down and try to unlock your desk')
#         if 'desk key' in Jon.items:
#             print('You unlock the desk.')
#             print('You gather all of your important documents')
#             print('You now have nothing tying you to this place.')
#             Jon.addItems('Important Documents')
#             study()
#         if 'desk key' not in Jon.items:
#             print('You try to unlock the desk but it wont budge.')
#             print('You need to go find the key!')
#             study()
#             stars()

# #CLOSING VENT
#     elif studyInput == '2':
#         sleep(3)
#         print('You walk over and firmly close the vent.')
#         sleep(3)
#         print('You feel safer while in this room.')
#         sleep(2)
#         stars()
#         vent = 'closed'
#         print(vent)
#         study()


# #BOOKSHELF
#     elif studyInput == '3':
#         print('You walk over to your bookshelf')
#         print('One black book catches your eye')
#         sleep(4)
#         print('You hold the book in your hands and feel an ominous power')
#         print('''The title of the book reads:
        
#         Conjurings and Summonings of the Occult''')
#         sleep(3)
#         stars()
#         print('''Do you?
        
#         1. Open the book
#         2. Put it back''')
#         book = input('-->')
#         while book != '1'and book != '2':
#             input('Please open the book or put it back, Id put it back.')
#         if book == '1':
#             print('You open the book and darkness fills the office')
#             print('Out of a portal Garfield is summoned')
#             print('He now stands before you ready for one final fight. ')
#             stars()
#             stars()

#         elif book == '2':
#             print('You place the book back on the shelf')
#             print('I think you made the right choice...')
#             stars()
#             study()

#     # elif studyInput =='4':
#     #     chooseRoom()

# study()