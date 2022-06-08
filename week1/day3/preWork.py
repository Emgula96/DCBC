#listA= ['bash', 'python', 'html', 'css', 'javascript', 'sql']

def toDoList():
    print()
    todos=['petcat','gotowork', 'shop', 'go home', 'feedbear']
    count = 1
    for todo in todos:
        print('%d: %s' %(count,todo))
        count +=1
    print(todos)

toDoList()
while input("Would you like to add anything to the lsit (Y/N)? ").lower() != "n":
    add= input('Wehat else do you need to do today?')
    todos=['petcat','gotowork', 'shop', 'go home', 'feedbear']
    todos.append(add)
print(todos)
todos=['petcat','gotowork', 'shop', 'go home', 'feedbear']
count = 1
for todo in todos:
    print('%d: %s' %(count,todo))
    count +=1
