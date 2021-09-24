
f=open('nameList.txt','r')


nameSet={}
n=0
l=f.readline()
while l:
                      
    l=l.strip()
    #print(l) 
    if l in nameSet:
        nameSet[l]+=1
        #print('--',nameSet) 
    else:
        nameSet[l]=1
        #print(nameSet,'--') 
    l=f.readline()  


print(nameSet)

## как вариант - переписать на for x in f
