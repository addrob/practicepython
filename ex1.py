import datetime

name=input('ur name: ')
age=int(input('ur age: '))
year=datetime.datetime.now()
txt=100-age+year.year
print (txt)

rep=int(input('gimme another number: '))
print (str(txt)*rep)
i=0

while i<rep:
    print (100-age+year.year)
    i+=1

input("Press any key to exit...")
