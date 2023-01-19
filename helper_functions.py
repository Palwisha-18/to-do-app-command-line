def get_todos(filepath="todos.txt"):
    """ Returns list of todos from the todos file """
    with open(filepath, 'r') as file:
        to_dos = file.readlines()
    return to_dos


def write_todos(to_dos, filepath="todos.txt"):
    """ Stores list of todos to todos file """
    with open(filepath, 'w') as file:
        file.writelines(to_dos)
