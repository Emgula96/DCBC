from contextlib import AsyncExitStack


def action(choice):
    if choice == "1":
        print("You attacked the monsetr")
        return
    if choice != "1" or choice != "2" or choice != "3" or choice != " 4":
        print("Please make a choice of 1,2,3, or 4 only")
        return

choiceList = """""
    1. Attack
    2. Run
    3. Block
    4. Dip
"""

print(choiceList)
choice = input("What action do you want to do?")
action(choice)
