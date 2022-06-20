class sort(object):
    def __init__(self):
        pass
    def sort_num(self, List, Char=0, POS=0):
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
                        if num < List_in or num==List_in:
                            New_num_List.insert(i, num)
                            break

                        if i==(Len-1):
                            New_num_List.append(num)
                        continue
        return New_num_List
            #else:
               #return 'boo you suck'

    def sort_alpha(self, L, C, POS):
        ASCII_ver=[]
        for i in L:
            ord_i=ord(i[POS])
            if len(ord_i) != 3:
                ord_i += '0'*(3-ord_i)
            i=str(ord_i)+(i.lstrip(i[POS]))
            ASCII_ver.append(i)
        sorted_ASCII=self.sort_num(ASCII_ver, C)
        return [int(chr(i[POS:POS+2].ltrip('0'))) for i in sorted_ASCII]

    def word_sort(self, L, C):
        import string
        Longest=0
        counter_column=0
        counter_row=0
        New_L=L
        for word in L:
            if len(word)>Longest:
                Longest=len(word)
        return self.sort_alpha(L, C, 0)



