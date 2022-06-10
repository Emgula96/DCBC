from time import sleep
from sys import exit

def mainMenu():
    print("""
    1. Play
    2. Tutorial
    3. Quit""")

def Gamestart():


    print("""Welcome to Digital Crafts Disc Golf!
    
            Main Menu
    """)
    mainMenu()
    menuopt= input("Choose from the options above --> ")
    
    if menuopt == 'Play':
        Dcdg()
    
    elif menuopt == 'Tutorial':
        tutorial()
    
    elif menuopt == 'Quit':
        print("Goodbye.")
        exit(0)
    else: 
        if menuopt != "Play" or menuopt != "Tutorial" or menuopt != 'Quit':
            print("Please enter Play, Tutorial, or Quit")
    

Gamestart()
