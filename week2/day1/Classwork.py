# Create a class called User which consists of
#  (first_name, last_name) properties. 
# Create a class name Address which consists of 
# (street, city, state, zip_code) properties.


class user:
    def __init__ (self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.address = []

    def addAdress(self, address):
        self.address.append(address)
    
    def changeFirstName(self, newName):
        self.firstName = newName

class Address:
    def __init__(self, Street, City, State, zip):
        self.street = Street
        self.city =  City
        self.state = State
        self.zip = zip

    def __str__(self):
        print(f'{self.street}{self.city}{self.state}{self.zip}') 


home = Address('123 Sesame street','Sugarland', 'TX','12312')

Ethan = user('Ethan', 'Gula')


# # print(Ethan, home)
# Ethan.addAdress(home)
# print(Ethan.address[0])
