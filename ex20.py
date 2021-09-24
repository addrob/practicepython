print('Проверить наличие числа в Списке, используя бинарный поиск')

def bi_finder(x, target):
    index_x = len(x)
    while True: 
        index_x //= 2
        print (index_x)
        if target < x[index_x]:
            x = x[:index_x]
            print (x)
        elif target > x[index_x]:
            x = x[index_x:]
            print (x)        
        elif target == x[index_x]:
            return True
        else:
            return False

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 34]
target=int(input('Check if your number is invited to the party: '))
print (bi_finder(a, target))
        
            
        
