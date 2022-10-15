# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

field = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]


def draw_field():
    print(field[0], end=" ")
    print(field[1], end=" ")
    print(field[2])

    print(field[3], end=" ")
    print(field[4], end=" ")
    print(field[5])

    print(field[6], end=" ")
    print(field[7], end=" ")
    print(field[8])


def turn(field, step, sign):
    marker = False
    while marker == False:
        for i in range(len(field)):
            if field[i] == step:
                field[i] = sign
                marker = True
        if marker == True:
            break
        else:
            step = control(len(field), 'The cell is occupied. Choose another cell. ')

def check():
    win = ''
    for i in victory:
        if field[i[0]] == 'X' and field[i[1]] == 'X' and field[i[2]] == 'X':
            win = 'X'
        if field[i[0]] == 'O' and field[i[1]] == 'O' and field[i[2]] == 'O':
            win = 'O'
    return win

def control(mean, text):
    marker = False
    while marker == False:
        data = input(text)
        try:
            data = int(data)
            if data > 0 and data <= mean:
                marker = True
                return int(data)
        except None:
            marker == False


end = False
player1 = True
count = 0
draw_field()

while end == False:
    if player1 == True:
        sign = 'X'
        step = control(len(field), 'Your turn player1, input a digit from 1 to 9: ')
    else:
        sign = 'O'
        step = control(len(field), 'Your turn player2, input a digit from 1 to 9: ')

    turn(field, step, sign)
    draw_field()
    win = check()
    count += 1
    if win != '':
        end = True
        print(f'Winner is "{win}"')
    elif win == '' and count == 9:
        end = True
        print('There is no winner.')
    else:
        end = False

    player1 = not (player1)


