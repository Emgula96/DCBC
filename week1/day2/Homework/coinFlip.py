def coinFlip():
    import random
    rand = random.randint(1,2)
    print("You flip a coin...")
    if rand == 1:
        print("Its Tails")
    else:
        print("It's Head!")

coinFlip()
while input("Would you like to flip again? (Y/N)? ").lower() != "n":
    coinFlip()
print("Goodbye")