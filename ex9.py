import random


def compare(random_number, user_number):
    if int(user_number) > random_number:
        print('too high')
        return False
    elif int(user_number) < random_number:
        print('too low')
        return False
    else:
        print('yup')
        return True


if __name__ == 'main':
    while True:
        number = random.randrange(1, 10)
        while True:
            user_input = input('guess a number 1-9:  ')
            if user_input == 'exit':
                break
            if compare(number, user_input):
                break
        if user_input == 'exit':
            break
