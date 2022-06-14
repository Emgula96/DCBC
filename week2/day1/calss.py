#classses and how to use them

# user = {
#     'key': 'value'
# }
# user['name'] = 'Amanda'
# #reasign


# rahmin = new Person()
# rahmin.speak()
# //'whats up'
# amanda = new Person()
# amanda.speak()
# // 'hello'


#barebones of a class and calling that class
class User:
    #name
    #height
    #siblings
    #weight
    #greeting
    def __init__(self, name, height, weight, siblings, greeting):
        self.name = name
        self.height = height
        self.weight = weight
        self.siblings = siblings
        self.greeting = greeting


rahmin = User('rahmin', '5.10ft', '300','4', 'yo')
olivia = User('Olivia', '5.7ft', '175','3', 'sup nerds')
print(rahmin)
print(olivia.name)

#constuctor
#what we want to do now is define a clsss with a conmstructor and then add 
# specific things to it that help us with our program

#the construcotr is the blue print of this clss only



