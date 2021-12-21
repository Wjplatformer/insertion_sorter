class sort(object):
    def __init__(self):
        pass
    def sort_num(List):
        num_List=List
        if not list(num_List):
            num_List=list(num_List)
        for i in range(len(num_List)):
            num=i
            if len(New_num_List)==0:
                New_num_List.append(num)
            else:
                for i in range(len(New_num_List)):
                    List_in=New_num_List[i]
                    if num < List_in or num==List_in:
                        New_num_List.insert(i, num)
                        break
                    else:
                        if i==(len(self.New_num_List)-1):
                            New_num_List.append(num)
                        continue
