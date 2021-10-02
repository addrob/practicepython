import string
import random


def password_generator(symbol_list):
    count = 0
    password = ''
    while count < 16:
        password += symbol_list[random.randrange(len(symbol_list))]
        count += 1
    return password


symbols = string.ascii_letters + string.digits + string.punctuation

if __name__ == '__main__':
    print('ur password: ' + password_generator(symbols))
