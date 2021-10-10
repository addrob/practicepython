import random


def user_input():
    while True:
        user_number = input('gimme a number 1000-9999: ')
        if user_number == 'stop':
            return user_number
        else:
            try:
                user_number = int(user_number)
                if user_number in range(1000, 9999):
                    return user_number
                else:
                    print('i need a number in range 1000-9999')
            except ValueError:
                print('i need a NUMBER!')


def cows_and_bulls(number):
    cows = 0
    bulls = 0
    user_number = user_input()
    while user_number != 'stop':
        symbol_index = 0
        user_number_str = str(user_number)
        for symbol in user_number_str:
            number_str = str(number)
            if symbol in number_str:
                if symbol == number_str[symbol_index]:
                    cows += 1
                else:
                    bulls += 1
            symbol_index += 1
        print(f'cows: {cows}')
        print(f'bulls: {bulls}')
        if user_number == number:
            print('you won!')
            break
        cows = 0
        bulls = 0
        user_number = user_input()


if __name__ == '__main__':
    cows_and_bulls(random.randrange(1000, 9999))
