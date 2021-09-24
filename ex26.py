
game =  [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

def line_checker(game):
    #смотрим горизонтальные
    for n in range(3):
        if game[n][0] != 0:
            if game[n][0] == game[n][1] == game[n][2]:
                return game[n,0]
    #смотрим вертикальные
    for n in range(3):
        if game[0][n] != 0:
            if game[0][n] == game[1][n] == game[2][n]:
                return game[0][n]
    #смотрим диагональные     
    if game[1][1] != 0:
        if game[0][0] == game[1][1] == game[2][2]:
             return game[1][1]
        elif game[1][1] == game[2][0] == game[0][2]:
            return game[1][1]
    return 0
        

print(line_checker(game))
