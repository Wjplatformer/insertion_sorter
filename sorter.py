import random

num_List=[]
New_num_List=[]

num='0'

def sort(num):
    global New_num_List
    if len(New_num_List)==0:
        New_num_List.append(num)
    else:
        for i in range(len(New_num_List)):
            List_in=New_num_List[i]
            if num < List_in or num==List_in:
                New_num_List.insert(i, num)
                break
            else:
                if i==(len(New_num_List)-1):
                    New_num_List.append(num)
                continue
                

while True:
    num=input('Place in a number. Enter any key that is not a number and stop. Enter R for 10 random numbers')
    if num.isnumeric(): 
        num_List.append(int(num))
    else:
        if num=='R':
            for i in range(10):
                num_List.append(random.randint(1, 10000000000))
        break

print(num_List)
print('='*50)
for i in range(len(num_List)):
    sort(num_List[i])
    
print(New_num_List)
print(f'sorted, length: {len(New_num_List)}, old collection length: {len(num_List)}')
    

