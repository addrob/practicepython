

fileName=str(input('say my name: \n',))
fileName=fileName + '.txt'
f=open(fileName, 'a')

x=int(input('gimme a number: \n'))

if x%2==0:
    f.write('even\n')
else:
        f.write('odd\n')

if x%4==0:
    f.write ('делится на 4\n')

num=int(input('gimme one more number: \n'))
check=int(input('and another one: \n'))

if num%check==0:
    f.write('делятся красиво!\n')
else:
        f.write('красиво не делятся\n')

f.close()
stop=input('')
        
## print('Напишите 1, чтобы создать файл, 2 чтобы вычислить делитель, 3 чтобы распарсить сайт')
## print('Напишите quit чтобы выйти')
## while inputStr!='quit':
##     if inputStr='1.':
##          создаём файл...
##     if inputStr='2.'
##          вычисляем делитель...
##     if inputStr='3.'
##          парсим сайт...
