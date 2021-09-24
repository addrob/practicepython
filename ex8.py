
a = []
while True:
    a.append(input('player1:  '))
    a.append(input('player2:  '))
    if a[0] == a[1]:
        print('draw')
    elif ('sciccors' and 'rock') in a:
        print('rock')
    elif ('sciccors' and 'paper') in a:
        print('scissors')
    elif ('paper' and 'rock') in a:
        print('paper')
    a.clear()
    key = input('wanna continue? y/n:  ')
    if key == 'n':
        break
git config --global user.email "addrob@inbox.ru"
git config --global user.name "addrob"