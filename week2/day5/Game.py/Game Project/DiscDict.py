
# speed = {Discdisc}[0]

# Discdist = {

#     'Destroyer': {12, 5, -1, 3},

#     'Wraith':  {11, 5, -1, 3}


# }

# #user type in speed
# whatDisc = 
# newSpeed = 

# for item in discDisct.key():







import string


discDict = {'Destroyer': [12, 5, -1, 3], 'Wraith': [11, 5, -1, 3], 'Thunderbird': [9, 5, 0, 2], 'Savant': [9, 5, -1, 2], 'Leopard 3': [7, 5, -2, 1], 'Firebird': [8, 4, 0, 4], 'Roc 3': [5, 4, 0, 3], 
'xcaliber': [15, 5, 0, 4], 'Shryke': [13, 6, -2, 2], 'Teebird 3': [8, 4, 0, 2], 'Method': [5, 5, 0, 3], 'Cloudbreaker': [12, 5, -1, 3], 'Eagle': [7, 5, -1, 3], 'Exodus': [7, 5, -1, 2], 
'Buzz': [5, 5, -1, 1],'Roadrunner': [9, 5, -4, 1], 'Sidewinder': [9, 5, -3, 1], 'Polecat': [1, 3, 0, 0], 'Nova': [2, 3, 0, 0], 'Kc Aviar ': [2, 3, 0, 2], 'Nuke': [13, 5, -1, 3], 'Hades': [12, 6, -3, 2],
'Anax': [10, 6, 0, 3], 'Raptor': [9, 4, 0, 3], 'Vulture': [10, 5, 0, 2], 'Mantis': [8, 4, -2, 2], 'Wasp': [5, 3, 0, 2], 'Malta': [5, 4, 1, 3],'Justice': [5, 1, 1, 4], 'Sol': [4, 5, -3, 0],
'Avenger SS': [10, 5, -3, 1], 'Meteor': [5, 5, -3, 1], 'Luna': [3, 3, 0, 3], 'Raider': [13, 5, -1, 3], 'Captain': [13, 5, -2, 2], 'Felon': [9, 3, 0, 4], 'Emac Truth': [5, 5, 0, 2],
'Truth': [5, 5, -1, 1], 'Getaway': [9, 5, -1, 3], 'Pa-3': [3, 4, 0, 1], 'A3': [4, 4, 0, 3], 'M3': [5, 5, -1, 2], 'H3V2': [11, 5, -1, 2], 'D2': [12, 6, -1, 3], 'D3': [12, 6, -2, 2],
'Fierce': [3, 4, -2, 2], 'Zone': [4, 3, 0, 3], 'Hex': [5, 5, -1, 1], 'Envy': [3, 3, 0, 2], 'Nomad': [2, 4, 0, 2], 'Reactor': [5, 5, -1, 2], 'Escape': [9, 5, -1, 2]}
discNum = []
discName = []
moreDiscs = ""


def prepDiscRef ():
    name = input('What is the name?\n')
    speed = int(input("What do you want the disc speed to be?\n"))
    glide = int(input("What do you want the disc glide to be?\n"))
    turn = int(input("What do you want the disc turn to be?\n"))
    fade = int(input("What do you want the disc fade to be?\n"))
    
    
    entry1 = [speed,glide,turn,fade]
    discNum.append(entry1)
    discName.append(name)

    discDict = dict(zip(discName, discNum))
    print(discDict)

prepDiscRef()
while moreDiscs.lower() != "n":
    moreDiscs = input("Want more discs? Y/N \n")
    prepDiscRef()


