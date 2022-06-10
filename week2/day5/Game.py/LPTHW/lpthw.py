from sys import exit
from time import sleep
print("You enter a dark room with four doors.")

def doorNum():
    print(
    """"
    Do you go to  
    Door # 1  
    Door # 2
    Door # 3
    Door # 4
""")
doorNum()

door = input("--> ")

if door == "1":
    print("There's a giant bear! He is eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print( "2. Scream and run away.")
    
    bear = input("--> ")

    if bear =="1":
        print(" The bear eats your face off! You lose.")
        exit
        
    elif bear ==("2"):
        print("The bear eats your legs off. You bleed out.")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("The bear runs away")

elif door == '2':
    print ("You stare into the endless abyss at Cthulhu's retina' ")
    print('1.Blueberries.')
    print('2.Yellow Jacket clothspins.')
    print('3. Understanding space time complecxity')

    insanity = input('-->')
    
    if insanity == '1' or insanity =='2':
        print('Your body survives powered by a mind opf jello')
        print('Goodjob')
    else:
        print('The insanity rots your eyes into a pool of muck')
        print('Good Job')

elif door == '3':
    print('You step through the door and begin falling')
    sleep(2)
    print('You are still falling')
    sleep(2)
    print('Yup, still falling')
    sleep(2)
    print('You land on a pile of matresses safely and walk out the exit.')
elif door == '4':
    print('You enter another room full of doors')
    doorNum()
    cycle = input('-->')
    if cycle in ["1","2","3","4"]:
    # cycle = int(input('-->'))
    # if cycle <= 4:
        print('You continually loop through this cyle of doors..')
        sleep(3)
        print('FOREVER')

    else:
        print("A black hole opens in the floor and you get torn apart")

else: 
    print('You stumble around and fall on a knife and die. Youre Dead!')

