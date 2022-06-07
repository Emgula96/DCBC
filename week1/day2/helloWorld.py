# Function
# 1. function name
# 2. funcitioin Body
# 3. function arguments

print("Hello World")

# Syntax in python for a function is def
# def "Function name" ():
# indent
def sayHi():
    print("Hi")
    print("This is the body")

 # Run a function "functionName()"
sayHi()

# Variables
teacher = "Ethan"
# String ""
# "house"
# "1"
# "Print()"
#Boolean true/false
True
False 
true = True
callie = False
# intergers (whole numbers)
number = 1
# Float
floatNumber = 1.75
jankyFloat = 3.2e213


# List/Arrays
students = ["Ethan", "Blake", True, 3]
#Acess list by using index of the list
#Start at 0  UX/UI start at 1 remmeber to switch over
#-1 would print 3 -numbers start from the back
print(students[1])

#Dictionary/Object
#Variable that has {}
randomData = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "age": "old",
    "number": 1,
    "hot": True,
    "students": ["Ethan", "Carlos"],
    "sorry": [{"name": "Joe"}]

}

print(randomData["hot"])
print(randomData["students"][0])


data = {
    "president":{
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "location": ["South America"]
    }
}
#print name and location of mr president
print(data["president"]["name"])
print(data["president"]["location"][0])
