import random
from sort_alg import sort
val='0'
NL=[]           
Char=''

while True:
    val=input('Place in anything. Press R for 100 random numbers. enter | to end . You can only place all Characters or all interger numbers')
    if val=='|':
        Cyn=input('Please place in D if you want decrement, if not, hit return')
        if Cyn=='D':
            Char=Cyn
        break
    else:
        if val != 'R' and val.isalpha():
            print('invalid')
            break
        else:
            if val=='R':
                for i in range(100):
                    NL.append(random.randint(1, 1000))
            else:
                NL.append(int(val))

print(NL)
print('='*50)

S=sort()

print(S.sort_num(NL, Char))

