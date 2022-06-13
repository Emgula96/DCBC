

from time import sleep







# hideSceneOne()
# realCom = input('I wanna fight -->')
# if realCom == 'fight':
#     fightSceneOne()
# else: 
#     print('FUCK YOU ')

def hallWayTwo():
    print("""
        Nice! You have aquired a blaster pistol from the weapons rack
        """)
    sleep(2)
    print("""
        There is another hallway coming up in front of you.
        Be careful. There is a barracks system attached right
        to this hallway. Enemies can come out whenever 
        """)
    sleep(2)
    print("""
        Oh no.. The door opened up..
        I see two heat signatures coming through the door,
        You have to be quick. You can either hide,
        or you can fight. If there are only two of them,
        and you take them out, you may be able to upgrade your weapon.
        """)
    playerAction = input("""
        Do you want to fight or hide?
        """)
    while playerAction != 'fight' and playerAction != 'hide':
        playerAction = input('Choose only hide or run, quickly!!')
    if playerAction == "fight":
        fightSceneOne()
        # Make another function for the "Fight" scene and invoke it here
    elif playerAction == "hide":
        print("""
            Get behind that pillar to the right!
            That is the only bit of cover I can see for you.
            """)
        hideSceneOne()
            # Make another function for the "Hide" scene and invoke it here

def fightSceneOne():
    print("""
    They have auto blasters! Be accurate and hit your shots!
        """)
    print("""
        *Two Stormtroopers round the hallway unaware of you*
        """)
    sleep(2)
    print("""
        Stormtrooper 1: 'Yo bro why was... Wait.. How did he get out?!
        """)
    sleep(1.5)
    print("""
    Stormtrooper 2: 'I'm not sure..
        He has a blaster! BLAST EM!
        """)
def hideSceneOne():
    print("""
    *Two stormtroopers round the hallway unaware of you*
        """)
    sleep(1.5)
    print("""
    Stormtrooper 1: 'Yo bro why was Darth Vader being all moody today'
        """)
    sleep(.5)
    print("""
        'Bro I have no clue whatsoever he just seemed like an absolute b**** toda..
        """)
    sleep(.5)
    print('''

        *You peek out of your hiding space and see both stormtroopers being force choked out of the blue*

        ''')

hallWayTwo()