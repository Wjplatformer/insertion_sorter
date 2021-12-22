import random
from sort_alg import sort
num='0'
NL=[]           
Char=''

while True:
    num=input('Place in a number. Enter any key that is not a number and stop. Enter R for 10 random numbers')    
    if num.isnumeric(): 
        NL.append(int(num))
    else:
        Cyn=input('Please place in D if you want decrement, if not, hit return')
        if Cyn=='D':
            Char=Cyn
        if num=='R':
            for i in range(100):
                NL.append(random.randint(1, 1000))
        break

print(NL)
print('='*50)

Snum=sort()
print(Snum.sort_num(NL, Char))
    

