def insert(*args):
    global lista
    for i in args:
        lista = args


argu = insert('A', 'B')

print(argu)