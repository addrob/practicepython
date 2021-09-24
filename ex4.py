
def divisors(number):
    x = range(1, number+1)
    divisors_list = []
    for n in x:
        if number%n == 0:
            divisors_list.append(n)
    return divisors_list

number = int(input())

print(divisors(number))