import os

board_state = { 1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' ' }

def check_row(index1,index2,index3):
    if board_state[index1] == board_state[index2] == board_state[index3] and board_state[index1] != ' ':
        return board_state[index1]
    else:
        return False

def check_win(board_state,debug=False):
    # 123
    # 456
    # 789
    if debug:
        print(board_state)
        print_board(board_state)
    return check_row(1,2,3) or \
        check_row(4,5,6) or \
        check_row(7,8,9) or \
        check_row(1,4,7) or \
        check_row(2,5,8) or \
        check_row(3,6,9) or \
        check_row(1,5,9) or \
        check_row(7,5,3)

def clear_board():
    global board_state
    board_state = { 1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' ' }


def print_board(board_state):
    print('''
{:^3}|{:^3}|{:^3}
---+---+---
{:^3}|{:^3}|{:^3}
---+---+---
{:^3}|{:^3}|{:^3}
'''.format(board_state[1],board_state[2],board_state[3],board_state[4],board_state[5],board_state[6],board_state[7],board_state[8],board_state[9]))

player_1 = input("Player one name: ")
player_2 = input("Player two name: ")

player_1_sign = ''
player_2_sign = 'x'

while player_1_sign not in ('x','o'):
    player_1_sign = input(f"{player_1}, choose your sign, please ('x'|'o'): ")
    if player_1_sign == 'x': player_2_sign = 'o'

# player_1 = 'ArtemK'
# player_2 = 'Computer'
# player_1_sign = 'x'
# player_2_sign = 'o'

gamers = { player_1_sign:player_1, player_2_sign:player_2 }

player = player_1
player_sign = player_1_sign

# main loop
step = 1
while True:
    while not check_win(board_state):
        if step > 9: break
        os.system('clear')
        print_board(board_state)
        index = 0
        while index not in range(1,10):
            index = int(input(f'{player}, choose field (1-9): '))
            if 1 <= index <= 9 and board_state[index] != ' ':
                print("Waat, that's cell already played")
                index = 0
        board_state[index] = player_sign
        # change player
        step += 1
        if step % 2 == 0:
            player = player_2
            player_sign = player_2_sign
        else:
            player = player_1
            player_sign = player_1_sign
    os.system('clear')
    print_board(board_state)
    result = check_win(board_state)
    if result:
        print("Congrats {}, you won!".format(gamers[result]))
    else:
        print("That's a draw!")
    answer = ''
    while answer not in ('y','n'):
        answer = input("Play another one? (y|n): ")
    if answer == 'y':
        clear_board()
        step = 1
        player = player_1
        player_sign = player_1_sign
        continue
    else:
        print("Game over!")
        exit(0)
