#listA= ['bash', 'python', 'html', 'css', 'javascript', 'sql']

todos=['petcat','gotowork', 'shop', 'go home', 'feedbear']

def toDoList():
    print()
    count = 1
    for todo in todos:
        # print('%d: %s' %(count,todo))
        print(count,": ", todo)
        count +=1
    

toDoList()
while input("Would you like to add anything to the lsit (Y/N)? ").lower() != "n":
    add= input('Wehat else do you need to do today?')
    # todos=['petcat','gotowork', 'shop', 'go home', 'feedbear']
    todos.append(add)
toDoList()

