to_dos = []

while True:
    user_action = input("Select add, show, edit, completed or exit: ")
    user_action = user_action.strip()

    if user_action == 'add':
        to_do = input('Enter a to do: ')
        to_dos.append(to_do)
    elif user_action == 'show':
        for index, item in enumerate(to_dos):
            print(f'{index + 1}-{item}')
    elif user_action == 'edit':
        index = int(input('Enter index of the to do to edit: '))
        to_do = input('Enter new to do: ')
        to_dos[index - 1] = to_do
    elif user_action == 'completed':
        index = int(input('Enter index of the to do completed: '))
        to_dos.pop(index - 1)
    elif user_action == 'exit':
        print('Existing Application.')
        break

print('Bye!')
