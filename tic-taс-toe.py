import os
import random

board_state = { 1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' ' }

def check_row(index1,index2,index3):
    if board_state[index1] == board_state[index2] == board_state[index3] and board_state[index1] != ' ':
        return board_state[index1]
    else:
        return False

def check_win(board_state):
    # 123
    # 456
    # 789
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
    os.system('clear')
    print('''
{:^3}|{:^3}|{:^3}
---+---+---
{:^3}|{:^3}|{:^3}
---+---+---
{:^3}|{:^3}|{:^3}
'''.format(board_state[1],board_state[2],board_state[3],board_state[4],board_state[5],board_state[6],board_state[7],board_state[8],board_state[9]))

def get_random_player(gamers):
    return random.choice(gamers)

def get_other_player(starting_player, gamers_list):
    return gamers_list[gamers_list.index(starting_player)-1]
    # arr = gamers_list
    # arr.remove(starting_player)
    # return arr[0]

def get_second_sign(first_sign, signs):
    return signs[signs.index(first_sign)-1]
    # arr = signs
    # arr.remove(first_sign)
    # return arr[0]

def init_players(player_1, player_2):
    starting_player = get_random_player([player_1,player_2])
    second_player = get_other_player(starting_player,[player_1,player_2])
    signs = ['x','o']
    sign = ''
    while sign not in signs:
        sign = input(f"{starting_player}, choose your sign, please ('x'|'o'): ")
    return (starting_player, {starting_player: sign, second_player: get_second_sign(sign, signs)}, {sign: starting_player, get_second_sign(sign, signs): second_player })

player_1 = input("Player one name: ")
player_2 = input("Player two name: ")

starting_player, gamers, gamers_by_sign = init_players(player_1, player_2)

player = starting_player
# main loop
while True:
    while not check_win(board_state) and ' ' in board_state.values():
        print_board(board_state)
        index = 0
        while index not in range(1,10):
            index = int(input(f'{player}, choose field (1-9): '))
            if 1 <= index <= 9 and board_state[index] != ' ':
                print("Waat, that's cell already played")
                index = 0
        board_state[index] = gamers[player]
        player = get_other_player(player, list(gamers.keys()))
    print_board(board_state)
    result = check_win(board_state)
    if result:
        print("Congrats {}, you won!".format(gamers_by_sign[result]))
    else:
        print("That's a draw!")
    answer = ''
    while answer not in ('y','n'):
        answer = input("Play another one? (y|n): ")
    if answer == 'y':
        clear_board()
        player = get_random_player(list(gamers.keys()))
        continue
    else:
        print("Game over!")
        exit(0)
