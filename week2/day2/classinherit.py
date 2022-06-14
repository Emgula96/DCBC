


from unicodedata import name


class Employee:
    def __init__(self,name, department,role):
        self.name = name
        self.department = department
        self.role = role
    def talkAboutWork(self):
        print('man mondays am I right')

rahmin = Employee('Rahmin','engineering group','staff')
rayleigh = Employee('rayleigh','engineering group','staff')
carlos = Employee('carlos','engineering group','staff')
amanda = Employee('amanda','engineering group','staff')

class SuperEmployee(Employee):
    def __init__(self,name,department,role):
        super().__init__(name,department,role)
        self.security = 'top level'
    def leafAStandup(self):
        print("hey guys lets start our standup")
    pass
stacy = SuperEmployee('Stacy','Engineering group', 'Staff III')

carlos.talkAboutWork()




class Parents():
    def __init__(self, first,last,eyeColor,hairColor, ):
        self.first = first
        self.last = last
        self.eyeColor = eyeColor
        self.haircolor = hairColor

Amy = Parents('Amy', 'Gula','green', 'blonde')
Steve = Parents('Steve', 'Gula','blue','blonde')

class Child(Parents):
    def __init__(self,first,last,eyeColor,hairColor,videoGames):
        super().__init__(first ,last,eyeColor, hairColor)
        self.videoGames = videoGames

Ethan = Child('Ethan','Gula','Green','Blonde','League of Le')

class sibiling(Child):
    def __init__(self,first,last,eyeColor,hairColor,videoGames, annoyancelevel):
        super().__init__(first ,last,eyeColor,videoGames, hairColor)
        self.annoyanacelevel = annoyancelevel

Nick = sibiling('Nick','Gula','Blue','Blonde','Valorant',5)
Hayden = sibiling('Nick','Gula','Blue','Blonde','League of L',9)