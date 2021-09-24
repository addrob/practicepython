print('Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last')
print('elements of the given list. For practice, write this code inside a function.')

def pick(x):
    newList=[]
    newList.extend(x[0])
    newList.extend(x[-1])
    print(newList)

exList=list(input())
pick(exList)
