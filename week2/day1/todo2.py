# listOfTasks = []

# def greeting():
#     print('hello Nerd')


# def addItem():
    
    
    
    
    
    
    # itemToadd = input('what tod do you need to add?')
    # newTask.addItem(itemToadd)
    # newTask = Item(itemToadd)
    # listOfTasks.append(newTask)
    # for stuff in listOfTasks:
    #     print(stuff.name)

# class Item:

#     def __innit__(self, name):
#         self.name = name





# def menu():
#     choice = ''
#     while choice != 'Q':
#         choice = input('''
#         1. Press 1 Add a task
#         2. Press 2 Delete a task
#         3. Press 3 View all tasks
#         q  Press q to Quit
#         ''')
#         if choice == 1:
#             addTask()
#         elif choice == 2:
#             deleteTask()
#         elif choice == 3:
#             viewTasks()
        











class Todo:
    def __init__(self):
        self.toDoList = []
    
    def viewItems(self):
        if self.toDoList:
            count = 1
            for i in self.toDoList:
                for k, v in i.items():
                    print(f'{count}. {k}: {v}')
                    count +=1
        else:
            print('You currently have nothing to do\n')

    def addTask(self):
        task = input('What task would you like to add?\n')
        priority = input('''What is the priority of this task?
        1. High
        2. Normal
        3. Low\n''')
        if priority == '1':
            priority = 'High'
        elif priority == '2':
                priority = 'Normal'
        elif priority == '3':
            priority = 'Low'
        tododict = {}
        tododict[task] = priority
        self.toDoList.append(tododict)

    def deleteItem(self):
        ethantodo.viewItems()
        delete = int(input('What item do you need to delete, please enter the number?\n'))
        delIndex = delete - 1
        taskToDelete = self.toDoList[delIndex]
        del self.toDoList[delIndex]
        print(f'I just deleted {taskToDelete}.')

ethantodo = Todo()


while True:
    ethantodo.viewItems()
    userChoice = input('''\nWhat would you like to do, Type the number of the option you choose
    1. Add an item todo
    2. Delete an item
    3. Press q to quit\n''')
    if userChoice == '1':
        ethantodo.addTask()
    elif userChoice == '2':
        ethantodo.deleteItem()
    elif userChoice == 'q':
        print('Goodbye')
        break
    else:
        print('Please choose from the menu options')