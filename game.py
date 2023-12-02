def input_coord():
    index_x = int(input("Введите х координату: "))
    index_y = int(input("Введите y координату: "))
    return index_x, index_y


def hod_x(mass):
    while True:
        x, y = input_coord()
        if check_hod(mass, x, y):
            mass[x][y] = 'x'
            return True
        print('это поле занято')


def hod_0(mass):
    while True:
        x, y = input_coord()
        if check_hod(mass, x, y):
            mass[x][y] = '0'
            return True
        print('это поле занято')


def check_hod(mass, x, y):
    if mass[x][y] == '-':
        return True
    else:
        return False


def end_of_game(mass):
    if [mass[0][0], mass[1][1], mass[2][2]] == ['0', '0', '0']:
        print("выйграл 0")
        return True
    if [mass[2][0], mass[1][1], mass[0][2]] == ['0', '0', '0']:
        print("выйграл 0")
        return True
    if [mass[0][0], mass[1][1], mass[2][2]] == ['x', 'x', 'x']:
        print("выйграл x")
        return True
    if [mass[2][0], mass[1][1], mass[0][2]] == ['x', 'x', 'x']:
        print("выйграл x")
        return True

    for i in range(3):
        for check in [mass[i], [row[i] for row in mass]]:
            if check == ['0', '0', '0']:
                print("выйграл 0")
                return True
            if check == ['x', 'x', 'x']:
                print("выйграл x")
                return True
    return False


def print_pole(mass):
    for j in range(3):
        print(mass[j][0], " ", mass[j][1], " ", mass[j][2], "\n")


def game(mass):
    print_pole(mass)
    x_step = True
    while not end_of_game(mass):
        if x_step:
            print("ход x")
            if hod_x(mass):
                print_pole(mass)
        else:
            print("ход 0")
            if hod_0(mass):
                print_pole(mass)
        x_step = not x_step


pole = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
game(pole)
