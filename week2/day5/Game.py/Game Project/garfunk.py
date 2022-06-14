def gunOption1():
    print("You pick up the gun and shoot Garfield")
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
    print('Garfield now lunges forward and attacks causing you to drop the gun')
    Jon.hitByAttack(megaCat.attack)
    print(f'Your health is now {Jon.health}')
    sleep(3)
    print('''Would you like to 
    1. Shoot again
    2. Run to a new room''')






#           print('You fill Garfields pan')
#         print('''
# With malice in his voice, Garfield responds: 
# "This does not satiate me, human I demand more"''')
#         print('''What do you do?

#         1. Beg for mercy
#         2. Go to the store and buy more lasagna''')

#         gar2 = input('-->' )
#         if gar2 == '1':
#             print('Garfield responds "I am your mercy"')
#             print('Everything fades to black...')

#         elif gar2 == "2":
#             print('You manage to escape the house, and you set it on fire.')
#             print('''
# Ermerging from the flames are 40ft long bat wings, 
# Garfield flys towards the heavens never to be seen again.
#             ''')
#             sleep(10)
#             print('For now......')
#             #printbreak/end