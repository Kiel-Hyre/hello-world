def selfdividingNumbers(left,right):
    if 1 <= left <=right <= 1000 :
        bank = []
        for i in range(left,right+1) :
            for j in str(i) :
                if '0' in str(i) or int(i) % int(j) != 0 :
                    break
            else : bank.append(i)
        return bank
    return None
print(selfdividingNumbers(1,22))

'''    
arr = [ x for x in range(left,right+1) if '0' not in str(x)]
for i in arr :
    length = 0
    for j in str(i) :
        if int(i) % int(j) == 0 :
            length += 1
    if length == len(str(i)) :
        bank.append(i)
'''
