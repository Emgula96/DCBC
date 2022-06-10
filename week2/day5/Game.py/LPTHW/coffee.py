# we drink coffee, some of different sizes and strength
#  allows us to accept a "order", which will be a size of coffee and strength
# store data in a way that we can then do manipulation or calculation in another function
listOfOrders = []
moreCoffee = ""
def prepCoffee():
    cupSize = input("What kind of cup size do you want? sm,med,lg")
    strength = input("What kind of strength do you want? strong, med, light")
    order = {
        "size": cupSize,
        "strength": strength
    }
    listOfOrders.append(order)

def calcCoffeeGrind(listOfOrders):
    for order in listOfOrders:
        if order["size"] == "sm":
            print("You will need to grind 100grams of coffee")
        if order["size"] == "md":
            print("You will need to grind 150grams of coffee")
        if order["size"] == "lg":
            print("You will need to grind 200grams of coffee")

while moreCoffee.lower() != "n":
    prepCoffee()
    print(listOfOrders)
    moreCoffee = input("Want more coffee? Y/N")
calcCoffeeGrind(listOfOrders)