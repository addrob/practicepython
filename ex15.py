print('Написать программу, которая реверсирует строку по элементам')
def strReverser():
    txt=str(input('Tell me what you want to reverse\n'))
    words = txt.count(' ') + 1
    x = txt.split(' ')
    n=1
    new_txt = str('')
    while n <= words:
        new_txt = new_txt  + x[-n] +' '
        n+=1
        
    return new_txt

print(strReverser())
          
