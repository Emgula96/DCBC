from time import sleep
def stars():
    print('**********************************************************')

def endAlltxt():
        print('You pour gasoline all over the perimeter of the house')
        sleep(4)
        print('You use the lighter to light your cigarette')
        sleep(4)
        print('After a few puffs you decide this is the only way')
        print('You toss the lit cigarette to ignit the gas that has now soaked into the house.')
        print('You watch as your house burns to the ground. It\'s over.')
        sleep(8)
        print('''Ermerging from the flames are 40ft long bat wings, 
Garfield flies towards the heavens never to be seen again.
                ''')
        stars()
        print('''A piece of burnt parchment falls in front of you. You can barely make out what it says:
        "What comes next is all for you. Jon."''')
        stars()
        stars()
        stars()
        stars()
        stars()
        print('You survived! Thank you for playing!!')

def prefaceLog():
    print(''' 
    This game was inspired by the Youtube video: Garfield Gameboy'd and is a horror/adventure game featuring Garfield the cat. 
    Are you smart enough to out wit a 46 year old cat? lets find out in this decision based text game


    created by Ethan Gula with a very basic understanding of Python 3, copyright 2022
        ''')
    stars()



def study():
    print('You have arrived in the Study.')
    print('''What would you like to do?

    1. Close the open vent above the desk
    2. Inspect your desk
    3. Walk over to the bookshelf 
    ''')
    stars()
    studyInput = input('-->')
    while studyInput != '1' and studyInput != '2' and studyInput != '3':
        studyInput = input('Please only enter a number 1 - 3')
    if studyInput == '1':
        print('hi')
    elif studyInput == '2':
        print('hi')
    elif studyInput == '3':
        print('hi')


