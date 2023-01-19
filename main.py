import time

from helper_functions import get_todos, write_todos

print(f"It is {time.strftime('%b %d, %Y - %H:%M:%S')}")

while True:
    user_action = input("Select add, show, edit, completed or exit: ")
    user_action = user_action.strip()

    if user_action == 'add':

        new_to_do = input('Enter a to do: ') + '\n'
        to_dos = get_todos()
        to_dos.append(new_to_do)
        write_todos(to_dos)

    elif user_action == 'show':
        to_dos = get_todos()
        for index, item in enumerate(to_dos):
            item = item.strip('\n')
            print(f'{index + 1}-{item}')

    elif user_action == 'edit':

        index = int(input('Enter index of the to do to edit: '))
        to_do = input('Enter new to do: ') + '\n'
        to_dos = get_todos()
        to_dos[index - 1] = to_do
        write_todos(to_dos)

    elif user_action == 'completed':
        index = int(input('Enter index of the to do completed: '))
        to_dos = get_todos()
        to_dos.pop(index - 1)
        write_todos(to_dos)

    elif user_action == 'exit':
        print('Existing Application.')
        break
    else:
        print('You choosed an incorrect option. Try Again!')

print('Bye!')
