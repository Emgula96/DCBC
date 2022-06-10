from sys import exit
from time import sleep

def gold_room():
    print('This room is full of gold. how Much do you take?')

    choice = input('-->')
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead('Man, learn to type a number.')
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy, Bastard")

def bear_room():
    print("There is a bear here.")
    print("The Bear has a bunch of honey.")
    print("The fat bear is in front of a door")
    print("How are you going to move the bear??")
    print("Take the honey?, taunt bear?, Open door?".upper)
    bear_moved=False

    while True:
        choice = input('-->')
        if 'honey' in choice:
            dead('The bear looks at you, then slaps your face off.')
        elif choice == 'taunt bear' and not bear_moved:
            print('The bear moved from the door.')
            print('You may not walk through.')
            bear_moved = True
            sleep (2)
            gold_room()
        elif choice == "taunt bear" and bear_moved:
            dead("The Bear gets pissed off chews your leg off.")
        elif choice == 'Open Door' and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means.")
def dead(why):
    print(why, 'Game over!')
    exit(0)

bear_room()