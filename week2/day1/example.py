#class example

class Room:
#dimensions
#doors
#windows
#floor
#type/name
#contents
    def __init__(self,dimensions,doors,windows,flooring,name,contents):
        self.dimensions = dimensions
        self.doors = doors
        self.windows = windows
        self.flooring = flooring
        self.name = name,
        self.contents = contents
    
    def nameOfRoom(self):
        print(self.name)




Beddroom1 = Room('10x10x15', 1,3,'Cheap carpet', 'Ethans Room', ['tv','compuet','desk','dresser'])
# if Beddroom1.name == 'Ethans Room':
#     print('Ypu this is my room')

# for content in Beddroom1.contents:
#     print(content)

blakesRoom = Room('5x5x5', 0, 1, 'stone','Prison cell', ['empty pot', 'pile opf hay', 'chains','rat'] )

print(blakesRoom.name)


