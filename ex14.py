print('Написать программу, которая уберет дублирующиеся эл-ты Списка')
def exFun1(x):
    exList = []
    for n in x:
        if n not in exList:
            exList.append(n)
    return exList

def exFun2(x):
    exSet = set(x)
    return exSet

ourList = [1,2,1,2,1,2,1,3,2,4]
print('We have: ', ourList)
print('We get: ', exFun1(ourList))
print('And another one just for fun: ',exFun2(ourList))

