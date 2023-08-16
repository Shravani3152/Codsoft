todo_list = []

def addToDo(todo):
    todo_list.append(todo)

def editTodo(position, updated_todo):
    todo_list[position-1] = updated_todo 

def deleteTodo(position):
    todo_list.pop(position-1)

def showTodos():
    if len(todo_list) == 0:
        print('No todos added')
    else:
        print()
        print('-'*10)
        for i in range(len(todo_list)):
            print(str(i+1)+". "+todo_list[i])
        print('-'*10)
        print()
while True:
    print('Please select the given options')
    print('1. Add todo\n2. Modify Todo\n3. Delete Todo\n4. Show Todos\n5. Close App')
    action = int(input())
    if action == 1:
        todo = input('Enter todo: ')
        addToDo(todo)
    elif action == 2:
        if len(todo_list) == 0:
            print('No Todos found')
        else:
            showTodos()
            position = int(input('Enter position of todo: '))
            updated_todo = input('Enter modified todo: ')
            editTodo(position, updated_todo)
    elif action == 3:
        if len(todo_list) == 0:
            print('No Todos found')
        else:
            showTodos()
            position = int(input('Enter position of todo: '))
            deleteTodo(position)
    elif action == 4:
        showTodos()
    elif action == 5:
        print('Closing the app!')
        break 
