
def divisors(number):
    x = range(1, number+1)
    divisors_list = []
    for n in x:
        if number%n == 0:
            divisors_list.append(n)
    return divisors_list

def prime_check(number):
    if len(divisors(number)) <= 2:
        return True
    else:
        return False

number = int(input())

if prime_check(number):
    print('prime')
else:
    print('not prime')