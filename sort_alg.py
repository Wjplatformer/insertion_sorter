class sort(object):
    def __init__(self):
        pass
    def sort_num(self, List, Char):
        num_List=List
        New_num_List=[] 
        if not list(num_List):
            num_List=list(num_List)
        for i in range(len(num_List)):
            num=num_List[i]
            Len=len(New_num_List)
            if Len==0:
                New_num_List.append(num)
            else:
                for i in range(Len):
                    List_in=New_num_List[i]
                    if Char=='D':
                        if num > List_in or num==List_in:
                            New_num_List.insert(i, num)
                            break
                    else:
                        if num < List_in or  num==List_in:
                            New_num_List.insert(i, num)
                            break
                        
                    if i==(Len-1):
                        New_num_List.append(num)
                    continue
        return New_num_List
