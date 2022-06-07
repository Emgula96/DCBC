# import random
# my_random_number = random.randint(1, 10)

#Step 1
# print("I am thinking of a number between 1 and 10.")

# secretNum = 5
# while True:
#     guess = int(input("What's the number?"))
    
#     if guess == secretNum:
#         print("You win!")
#         break
#     elif guess != secretNum:
#         print("Nope, try again")




#         print("I am thinking of a number between 1 and 10.")

# #Step2
# secretNum = 5
# while True:
#     guess = int(input("What's the number?"))
    
#     if guess == secretNum:
#         print("You win!")
#         break
#     elif guess < secretNum:
#         print("Too low, try again!")
#     elif guess > secretNum:
#         print("Too High, try again!")

#step 3

def guessGame():

    print("I am thinking of a number between 1 and 10")
    import random
    my_random_number = random.randint(1, 10)
    guessLeft = 5


    while True:
        print(f"You have {guessLeft} guesses left")
        guess = int(input("What's the number?"))
        if guess == my_random_number:
            print("You win!")
            break
        elif guess < my_random_number:
            print("Too low, try again!")
            guessLeft -= 1
        elif guess > my_random_number:
            print("Too High, try again!")
            guessLeft -= 1
        if guessLeft == 0:
            print(" You have 0 guesses left, you lose, GET GOOD NERD!!!")
            break

guessGame()
while input("Would you like to play again? (Y/N)? ").lower() != "n":
    guessGame()
print("Goodbye")