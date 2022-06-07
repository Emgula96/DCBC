def diceRoll():
    
    print("Let's roll a dice!")
    sides= int(input("How many sides should it have?(2-20) "))
    import random
    my_random_number = random.randint(1, sides)
    print("It's rolling...")
    print("Its a", my_random_number)


diceRoll()
while input("Would you like to roll again? (Y/N)? ").lower() != "n":
    diceRoll()
print("Goodbye")