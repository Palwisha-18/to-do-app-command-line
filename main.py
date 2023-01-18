
while True:
    user_action = input("Select add, show, edit, completed or exit: ")
    user_action = user_action.strip()

    if user_action == 'add':
        to_do = input('Enter a to do: ') + '\n'

        with open('todos.txt', 'r') as file:
            to_dos = file.readlines()

        to_dos.append(to_do)

        with open('todos.txt', 'w') as file:
            to_dos = file.writelines(to_dos)

    elif user_action == 'show':
        with open('todos.txt', 'r') as file:
            to_dos = file.readlines()

        for index, item in enumerate(to_dos):
            item = item.strip('\n')
            print(f'{index + 1}-{item}')

    elif user_action == 'edit':
        index = int(input('Enter index of the to do to edit: '))
        to_do = input('Enter new to do: ') + '\n'

        with open('todos.txt', 'r') as file:
            to_dos = file.readlines()

        to_dos[index - 1] = to_do

        with open('todos.txt', 'w') as file:
            to_dos = file.writelines(to_dos)

    elif user_action == 'completed':
        index = int(input('Enter index of the to do completed: '))

        with open('todos.txt', 'r') as file:
            to_dos = file.readlines()

        to_dos.pop(index - 1)

        with open('todos.txt', 'w') as file:
            to_dos = file.writelines(to_dos)

    elif user_action == 'exit':
        print('Existing Application.')
        break

print('Bye!')
