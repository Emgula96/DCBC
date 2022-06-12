# we drink coffee, some of different sizes and strength
#  allows us to accept a "order", which will be a size of coffee and strength
# store data in a way that we can then do manipulation or calculation in another function
# listOfOrders = []
# moreCoffee = ""
# def prepCoffee():
#     cupSize = input("What kind of cup size do you want? sm,med,lg")
#     strength = input("What kind of strength do you want? strong, med, light")
#     order = {
#         "size": cupSize,
#         "strength": strength
#     }
#     listOfOrders.append(order)

# def calcCoffeeGrind(listOfOrders):
#     for order in listOfOrders:
#         if order["size"] == "sm":
#             print("You will need to grind 100grams of coffee")
#         if order["size"] == "md":
#             print("You will need to grind 150grams of coffee")
#         if order["size"] == "lg":
#             print("You will need to grind 200grams of coffee")

# while moreCoffee.lower() != "n":
#     prepCoffee()
#     print(listOfOrders)
#     moreCoffee = input("Want more coffee? Y/N")
# calcCoffeeGrind(listOfOrders)







listOfOrders = []
moreCoffee = ""
pourAmount = 0


def prepCoffeeOrder ():
    cupSize = input("What size coffee do you want? sm, med,lg\n")
    strength = input("What kind of strength do you want? normal, strong\n")
    order = {
        "size": cupSize,
        "caffiene": strength
    }
    listOfOrders.append(order)
def calcCoffeeGrind(listOfOrders):
    grindAmount = 0
    pourAmount = 0
    for order in listOfOrders:
        if order["size"] == 'sm':
            if order["caffiene"] == 'normal':
                grindAmount = grindAmount + 21
                pourAmount = pourAmount + 345
            if order["caffiene"] == 'strong':
                grindAmount = grindAmount + 23
                pourAmount = pourAmount + 345
        if order["size"] == 'med':
            if order["caffiene"] == 'normal':
                grindAmount = grindAmount + 28
                pourAmount = pourAmount + 450
            if order["caffiene"] == 'strong':
                grindAmount = grindAmount + 30
                pourAmount = pourAmount + 450        
        if order["size"] == 'lg':
            if order["caffiene"] == 'normal':
                grindAmount = grindAmount + 33
                pourAmount = pourAmount + 525
            if order["caffiene"] == 'strong':
                grindAmount = grindAmount + 35
                pourAmount = pourAmount + 525
    print(f"""
    You will need to grind {grindAmount} grams of coffee.
    Your first bloom pour will be {(grindAmount*2)} grams of hot water.
    Wait 45 - 60 seconds
    Your next pour will be up to {(pourAmount/2)} grams of hot water.
    Your final pour will be up to {pourAmount} grams of hot water.
    Let the water turn to delicious bean water and enjoy!
    """)

while moreCoffee.lower() != "n":
    prepCoffeeOrder()
    moreCoffee = input("Want more coffee? Y/N \n")

calcCoffeeGrind(listOfOrders)
