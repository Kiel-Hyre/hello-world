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
