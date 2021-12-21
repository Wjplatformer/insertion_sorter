import random

num_List=[]
New_num_List=[]

num='0'

def sort(num):
    print(f'entered{num}')
    global New_num_List
    if len(New_num_List)==0:
        print('first one inserted')
        New_num_List.append(num)
    else:
        for i in range(len(New_num_List)):
            print('entered loop')
            print(f'comparing{New_num_List[i]}')
            if num < New_num_List[i]:
                print(New_num_List[i])
                New_num_List.insert(i, num)
                print('inserted')
                break
            else:
                continue
                

while True:
    num=input('Place in a number. Enter any key that is not a number and stop')
    if num.isnumeric(): 
        num_List.append(int(num))
    else: break

print(num_List)
for i in range(len(num_List)):
    sort(num_List[i])
    
print(New_num_List)
    

