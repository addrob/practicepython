def player_turn(symbol):
    user_coordinate = input().split(',')
    if user_coordinate == 'stop':
        return False
    user_coordinate_int = []
    for n in user_coordinate:
        n = int(n)-1
        user_coordinate_int.append(int(n))
        print(user_coordinate_int)
    board_square =  board[user_coordinate_int[0]][user_coordinate_int[1]]
    if board_square != 0:
        print('not allowed')
        return False
    else:
        board[user_coordinate_int[0]][user_coordinate_int[1]] = symbol
        print(board)

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
print(board)

while True:
    player_turn('x')
    player_turn('o')